import os
import sqlite3
from datetime import date
from functools import wraps
from flask import Flask, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get("DATABASE_PATH", os.path.join(BASE_DIR, "student_success_hub.db"))
app = Flask(__name__)
app.config.update(
    SECRET_KEY=os.environ.get("SECRET_KEY", "local-development-key-change-before-deploy"),
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
)

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA foreign_keys = ON")
    return g.db

@app.teardown_appcontext
def close_db(_error):
    db = g.pop("db", None)
    if db is not None:
        db.close()

def init_db():
    os.makedirs(os.path.dirname(DATABASE) or ".", exist_ok=True)
    db = sqlite3.connect(DATABASE)
    db.execute("PRAGMA foreign_keys = ON")
    db.executescript("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        password_hash TEXT NOT NULL,
        created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
    );
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        title TEXT NOT NULL,
        course TEXT NOT NULL DEFAULT '',
        due_date TEXT NOT NULL,
        priority TEXT NOT NULL DEFAULT 'Medium',
        status TEXT NOT NULL DEFAULT 'Pending',
        created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
    );
    CREATE TABLE IF NOT EXISTS goals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        title TEXT NOT NULL,
        target_date TEXT NOT NULL,
        completed INTEGER NOT NULL DEFAULT 0,
        created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
    );
    """)
    db.commit()
    db.close()

def login_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if "user_id" not in session:
            flash("Please sign in to continue.", "info")
            return redirect(url_for("login"))
        return view(*args, **kwargs)
    return wrapped

@app.route("/")
def index():
    if session.get("user_id"):
        return redirect(url_for("dashboard"))
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        if not name or not email or len(password) < 8:
            flash("Enter your name and email, and use a password with at least 8 characters.", "error")
            return render_template("register.html")
        try:
            get_db().execute(
                "INSERT INTO users(name, email, password_hash) VALUES (?, ?, ?)",
                (name, email, generate_password_hash(password)),
            )
            get_db().commit()
        except sqlite3.IntegrityError:
            flash("An account with that email already exists.", "error")
            return render_template("register.html")
        flash("Account created. Please sign in.", "success")
        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        user = get_db().execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
        if user and check_password_hash(user["password_hash"], request.form.get("password", "")):
            session.clear()
            session["user_id"] = user["id"]
            session["user_name"] = user["name"]
            return redirect(url_for("dashboard"))
        flash("Email or password was incorrect.", "error")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    flash("You have been signed out.", "info")
    return redirect(url_for("index"))

@app.route("/dashboard")
@login_required
def dashboard():
    db = get_db()
    uid = session["user_id"]
    tasks = db.execute(
        """SELECT * FROM tasks WHERE user_id = ?
           ORDER BY CASE status WHEN 'Pending' THEN 0 ELSE 1 END, due_date, id""",
        (uid,),
    ).fetchall()
    goals = db.execute(
        "SELECT * FROM goals WHERE user_id = ? ORDER BY completed, target_date, id", (uid,)
    ).fetchall()
    completed = sum(task["status"] == "Completed" for task in tasks)
    upcoming = sum(
        task["status"] != "Completed" and task["due_date"] >= date.today().isoformat()
        for task in tasks
    )
    return render_template(
        "dashboard.html", tasks=tasks, goals=goals, total=len(tasks),
        completed=completed, upcoming=upcoming, today=date.today().isoformat()
    )

@app.route("/tasks/add", methods=["POST"])
@login_required
def add_task():
    title = request.form.get("title", "").strip()
    course = request.form.get("course", "").strip()
    due_date = request.form.get("due_date", "")
    priority = request.form.get("priority", "Medium")
    if not title or not due_date or priority not in {"Low", "Medium", "High"}:
        flash("Enter an assignment title, due date, and valid priority.", "error")
    else:
        get_db().execute(
            "INSERT INTO tasks(user_id, title, course, due_date, priority) VALUES (?, ?, ?, ?, ?)",
            (session["user_id"], title, course, due_date, priority),
        )
        get_db().commit()
        flash("Assignment added.", "success")
    return redirect(url_for("dashboard"))

@app.route("/tasks/<int:task_id>/status", methods=["POST"])
@login_required
def update_task(task_id):
    status = request.form.get("status", "")
    if status not in {"Pending", "Completed"}:
        flash("Invalid task status.", "error")
    else:
        get_db().execute(
            "UPDATE tasks SET status = ? WHERE id = ? AND user_id = ?",
            (status, task_id, session["user_id"]),
        )
        get_db().commit()
        flash("Assignment updated.", "success")
    return redirect(url_for("dashboard"))

@app.route("/tasks/<int:task_id>/delete", methods=["POST"])
@login_required
def delete_task(task_id):
    get_db().execute(
        "DELETE FROM tasks WHERE id = ? AND user_id = ?", (task_id, session["user_id"])
    )
    get_db().commit()
    flash("Assignment deleted.", "info")
    return redirect(url_for("dashboard"))

@app.route("/goals/add", methods=["POST"])
@login_required
def add_goal():
    title = request.form.get("title", "").strip()
    target_date = request.form.get("target_date", "")
    if not title or not target_date:
        flash("A goal title and target date are required.", "error")
    else:
        get_db().execute(
            "INSERT INTO goals(user_id, title, target_date) VALUES (?, ?, ?)",
            (session["user_id"], title, target_date),
        )
        get_db().commit()
        flash("Goal added.", "success")
    return redirect(url_for("dashboard"))

@app.route("/goals/<int:goal_id>/toggle", methods=["POST"])
@login_required
def toggle_goal(goal_id):
    db = get_db()
    goal = db.execute(
        "SELECT completed FROM goals WHERE id = ? AND user_id = ?",
        (goal_id, session["user_id"]),
    ).fetchone()
    if goal:
        db.execute(
            "UPDATE goals SET completed = ? WHERE id = ? AND user_id = ?",
            (0 if goal["completed"] else 1, goal_id, session["user_id"]),
        )
        db.commit()
        flash("Goal progress updated.", "success")
    return redirect(url_for("dashboard"))

@app.route("/goals/<int:goal_id>/delete", methods=["POST"])
@login_required
def delete_goal(goal_id):
    get_db().execute(
        "DELETE FROM goals WHERE id = ? AND user_id = ?", (goal_id, session["user_id"])
    )
    get_db().commit()
    flash("Goal deleted.", "info")
    return redirect(url_for("dashboard"))

@app.errorhandler(404)
def not_found(_error):
    return render_template("404.html"), 404

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)
