# Student Success Hub — Software Engineering Project Report

**Team members:** Anderson Peterkin and Azaevion Neal  
**Course:** Software Engineering  
**Instructor:** [Insert instructor name]  
**Submission date:** [Insert date]  
**GitHub repository:** [Insert actual repository URL]  
**Public application URL:** [Insert verified deployment URL]

> Submission integrity note: This is a report draft aligned to the assignment brief. Before submitting, replace every bracketed placeholder, update team contributions to reflect actual work, and add real deployment/GitHub evidence. Do not state that the app is publicly deployed until you have deployed and tested it.

## 1. Introduction
Student Success Hub is a web application designed to help college students manage academic responsibilities in one location. Students can record assignments, associate them with courses, set due dates and priorities, create academic goals, and monitor progress from a personal dashboard. The project applies software engineering practices through requirements definition, architecture design, implementation, automated testing, version control, containerization, and cloud deployment preparation.

## 2. Opportunity and problem
College students often track assignments and personal academic goals across separate tools, notebooks, learning-management systems, and calendars. Switching between locations can make it harder to see the complete workload. Student Success Hub addresses this organizational problem with a focused dashboard for assignment and goal tracking. The intended users are college students who want a lightweight planning tool.

## 3. Product vision
**For** college students who need a clearer way to organize academic work, **Student Success Hub is** a student productivity web application **that** centralizes assignment tracking and academic goal management. **Unlike** scattered notes and separate task lists, **the product** provides a personal dashboard that combines due dates, priorities, completion status, and goal progress.

## 4. Features
1. Account registration with unique email.
2. Sign-in and sign-out.
3. Protected personal dashboard.
4. Assignment creation with course, due date, and priority.
5. Assignment completion and reopening.
6. Assignment deletion.
7. Academic goal creation with target date.
8. Goal completion tracking.
9. Goal deletion.
10. Dashboard workload summary.

## 5. User stories and scenarios
The ten user stories and five user scenarios are documented in `USER_STORIES_AND_SCENARIOS.md`. They describe registration, authentication, assignment organization, completion tracking, and academic goals. Acceptance criteria define expected access control, persistence, validation, and ownership behavior.

## 6. Software architecture
The browser communicates with a Flask application over HTTP. Flask routes handle authentication, assignment operations, and goal operations. HTML/Jinja templates and CSS render the user interface. SQLite stores users, tasks, and goals. Passwords are hashed with Werkzeug. Docker packages the application and Gunicorn serves it in deployment. See `ARCHITECTURE.md` for the architecture diagram, database entities, and routes.

## 7. Implementation
The application is implemented with Python, Flask, SQLite, HTML, CSS, and Jinja. It includes registration, login, a session-protected dashboard, assignment CRUD operations, academic goal operations, summary counts, and per-user record filtering. SQL statements use parameters. Passwords are stored as hashes. The code and setup steps are included in the source package.

## 8. Testing
Automated tests are provided using Python's `unittest` framework. The test suite covers the home page, account registration and login, duplicate registration, protected dashboard, task lifecycle, goal lifecycle, and user data isolation. The team should rerun the tests and paste or attach the actual output from the final version. Add manual browser and deployment test evidence before submission.

## 9. Deployment
The repository includes a Dockerfile and Render Blueprint (`render.yaml`). The deployment plan is to connect the GitHub repository to Render, create the service, verify the public URL, register a test account, and confirm task and goal data persist. **Deployment status: [Update after actual deployment].** Public URL: [Insert verified URL]. Add a screenshot of the live app.

## 10. Challenges
Potential project challenges include selecting a manageable scope, defining clear user stories, connecting web forms to persistent database records, protecting private user data, and preparing the application for containerized deployment. Replace this paragraph with the actual challenges the team encountered and how you resolved them.

## 11. Team contributions
Complete this section using actual work and GitHub evidence.

| Team member | Actual contribution | Evidence |
|---|---|---|
| Anderson Peterkin | [Describe work actually completed] | [Commit hash / file / screenshot] |
| Azaevion Neal | [Describe work actually completed] | [Commit hash / file / screenshot] |

Both teammates should make genuine commits and participate in testing and review. Do not claim equal or specific contributions unless that is accurate.

## 12. Lessons learned
The project demonstrates how requirements connect to implementation and testing. User stories help define the functions students need; architecture clarifies how the browser, application, and database work together; automated tests provide repeatable checks for important behaviors. Containerization makes the application easier to run consistently, while deployment requires attention to configuration, secrets, persistence, and verification. Add specific lessons each teammate learned.

## 13. Conclusion
Student Success Hub provides a working foundation for a student-focused academic organizer. The current implementation focuses on account access, assignment tracking, academic goals, and a dashboard summary. Future enhancements could include calendar integration, email reminders, recurring tasks, analytics, and integration with campus learning platforms. Final submission should include the verified repository and public application links plus screenshots that demonstrate the deployed system.
