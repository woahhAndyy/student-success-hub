import os
import tempfile
import unittest
from app import app, init_db

class StudentSuccessHubTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.db_path = os.path.join(self.tmp.name, "test.db")
        app.config["TESTING"] = True
        app.config["SECRET_KEY"] = "test-secret"
        app.config["DATABASE"] = self.db_path
        import app as app_module
        app_module.DATABASE = self.db_path
        init_db()
        self.client = app.test_client()

    def tearDown(self):
        self.tmp.cleanup()

    def register_and_login(self, email="student@example.edu"):
        self.client.post("/register", data={
            "name": "Test Student", "email": email, "password": "strongpass123"
        }, follow_redirects=True)
        return self.client.post("/login", data={
            "email": email, "password": "strongpass123"
        }, follow_redirects=True)

    def test_home_page_loads(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Make every semester", response.data)

    def test_registration_and_login(self):
        response = self.register_and_login()
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Assignments", response.data)

    def test_duplicate_registration_is_rejected(self):
        self.client.post("/register", data={"name":"A","email":"same@x.com","password":"password123"})
        response = self.client.post("/register", data={"name":"B","email":"same@x.com","password":"password123"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"already exists", response.data)

    def test_dashboard_requires_login(self):
        response = self.client.get("/dashboard")
        self.assertEqual(response.status_code, 302)
        self.assertIn("/login", response.location)

    def test_task_add_complete_and_delete(self):
        self.register_and_login()
        self.client.post("/tasks/add", data={
            "title":"Database project", "course":"CSC 4355",
            "due_date":"2027-01-20", "priority":"High"
        })
        response = self.client.get("/dashboard")
        self.assertIn(b"Database project", response.data)
        self.client.post("/tasks/1/status", data={"status":"Completed"})
        response = self.client.get("/dashboard")
        self.assertIn(b"Completed", response.data)
        self.client.post("/tasks/1/delete")
        self.assertNotIn(b"Database project", self.client.get("/dashboard").data)

    def test_goal_add_toggle_delete(self):
        self.register_and_login()
        self.client.post("/goals/add", data={"title":"Study three times weekly","target_date":"2027-02-01"})
        self.assertIn(b"Study three times weekly", self.client.get("/dashboard").data)
        self.client.post("/goals/1/toggle")
        self.client.post("/goals/1/delete")
        self.assertNotIn(b"Study three times weekly", self.client.get("/dashboard").data)

    def test_user_cannot_modify_another_users_task(self):
        self.register_and_login("first@example.edu")
        self.client.post("/tasks/add", data={"title":"Private task","course":"CSC","due_date":"2027-01-01","priority":"Medium"})
        self.client.get("/logout")
        self.register_and_login("second@example.edu")
        self.client.post("/tasks/1/delete")
        self.assertNotIn(b"Private task", self.client.get("/dashboard").data)

if __name__ == "__main__":
    unittest.main()
