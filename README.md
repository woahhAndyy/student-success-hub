# Student Success Hub

**Team:** Anderson Peterkin and Azaevion Neal  
**Course:** Software Engineering  
**Project type:** Cloud-based student productivity web application
**GitHub repository url:** https://student-success-hub-9sqm.onrender.com 
## Overview
Student Success Hub gives college students one place to organize assignments, due dates, course labels, priority, and academic goals. A personal dashboard summarizes total assignments, completed assignments, and upcoming work.

## Implemented features
1. Account registration with unique email addresses.
2. Sign-in and sign-out.
3. Protected personal dashboard.
4. Create assignments with course, due date, and priority.
5. Mark assignments complete or reopen them.
6. Delete assignments.
7. Create academic goals with target dates.
8. Mark goals complete/incomplete and delete them.
9. Dashboard summary counts.
10. Per-user data isolation for task and goal operations.

## Technology
- Python 3.12
- Flask
- SQLite
- HTML / CSS / Jinja templates
- Werkzeug password hashing
- unittest
- Docker + Gunicorn
- Render deployment configuration (`render.yaml`)

## Run locally
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```
Open http://127.0.0.1:5000. Create an account to use the dashboard.

## Run automated tests
```bash
python -m unittest discover -s tests -v
```

## Run with Docker
```bash
docker build -t student-success-hub .
docker run --rm -p 5000:5000 -e SECRET_KEY="replace-with-a-long-random-secret" student-success-hub
```
Open http://localhost:5000. The provided Dockerfile stores the SQLite database at `/data/student_success_hub.db`. For persistent data, mount a Docker volume at `/data`.

## Deploy on Render
1. Push this repository to GitHub.
2. In Render, choose **New → Blueprint** and connect the repository containing `render.yaml`.
3. Review the service and persistent disk configuration, then create it.
4. Wait for deployment and open the generated `onrender.com` URL.
5. Register a test account and verify task and goal operations.
6. Keep the public URL in the report and slides. Do not claim deployment until you have verified it.

**Important:** The Render free web service may sleep when idle. The persistent disk is configured in `render.yaml`; confirm plan availability and disk billing in your Render account before deployment.

## GitHub workflow
- Create a repository named `student-success-hub`.
- Commit in small logical increments (initial Flask skeleton, authentication, assignment CRUD, goals, UI, tests, deployment).
- Both teammates should make genuine commits and review each other's work.
- Do not upload `.env`, secrets, database files, or passwords.

## Security and limitations
Passwords are stored as Werkzeug password hashes, not plaintext. Database statements use parameterized SQL. Task and goal routes scope database operations to the signed-in user's ID. This is a class-project prototype, not a production student information system. It does not integrate with a university LMS, send reminder emails, or provide calendar synchronization. Production hardening would include CSRF protection, password reset, rate limiting, stricter input/date validation, HTTPS enforcement, backups, and a managed database.

## Team work log
Fill this table with what actually happened. Do not claim contributions or commits that did not occur.

| Team member | Actual work completed | Evidence (commit, file, screenshot) |
|---|---|---|
| Anderson Peterkin | Created and organized the GitHub repository; configured the public Render deployment and application URL; created the PowerPoint presentation and README documentation; prepared project documentation; performed live browser testing, including registration, login, logout, task creation, and task persistence checks. | GitHub repository and commit history; live Render application; project report; PowerPoint presentation; README; browser testing screenshots.<img width="1366" height="768" alt="Screenshot 2026-11-17 10 16 13 AM" src="https://github.com/user-attachments/assets/c5e39dca-f35f-4298-b5ae-9bbe1c5a14bb" />
<img width="1366" height="768" alt="Screenshot 2026-11-17 10 11 37 AM" src="https://github.com/user-attachments/assets/b1397f04-5e1b-463f-b661-cdc127479916" />
<img width="1366" height="768" alt="Screenshot 2026-11-17 10 03 03 AM" src="https://github.com/user-attachments/assets/9269cef1-295a-4ee8-9b12-465fe9fbb062" />
<img width="1366" height="768" alt="Screenshot 2026-11-17 10 00 01 AM" src="https://github.com/user-attachments/assets/bfcbe68e-e4c7-4d25-84c4-16b9813921a5" />
<img width="1366" height="768" alt="Student_Success_Hub_Login_Test" src="https://github.com/user-attachments/assets/46424244-b9e8-489c-9b97-9fa4870f99c9" />
<img width="1366" height="768" alt="Student_Success_Hub_Task_Test" src="https://github.com/user-attachments/assets/f90179f7-6994-47e9-ad80-3b025d499fa3" /><img width="1366" height="768" alt="Screenshot 2026-11-17 10 22 01 AM" src="https://github.com/user-attachments/assets/c93cac29-4b70-421b-bd50-312a9b23fad2" />


| Azaevion Neal | Helped with testing and debugging the files, as well as project distribution and making sure files weree in the right place for successful output test. | <img width="1366" height="768" alt="Screenshot 2026-11-17 10 20 11 AM" src="https://github.com/user-attachments/assets/9cfcb5ed-fa4d-45df-8dbb-5f748d085552" />
<img width="1366" height="768" alt="Screenshot 2026-11-17 10 19 39 AM" src="https://github.com/user-attachments/assets/3f638c01-62b2-43a9-bad6-a442e8344092" />
<img width="1366" height="768" alt="Screenshot 2026-11-17 10 17 51 AM" src="https://github.com/user-attachments/assets/2c2f955a-e509-4268-ba95-1256c63083ee" />
|

## Submission checklist
- [ ] Create the GitHub repository and add its real URL.
- [ ] Both teammates contribute and review commits.
- [ ] Run the test command and save the actual result.
- [ ] Build and run the Docker image.
- [ ] Deploy to Render and test the public URL.
- [ ] Capture screenshots of home page, registration/login, dashboard, assignment workflow, goal workflow, GitHub commits, test output, Docker build, and deployed app.
- [ ] Export final report and presentation after inserting real links and evidence.
