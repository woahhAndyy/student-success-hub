# Requirements: User Stories and Scenarios

## User-facing features
1. Account registration.
2. Secure sign-in and sign-out.
3. Personal dashboard.
4. Assignment creation with course, due date, and priority.
5. Assignment completion/reopening.
6. Assignment deletion.
7. Academic goal creation and target date.
8. Goal completion tracking.
9. Goal deletion.
10. Summary counts for total, completed, and upcoming assignments.

## Ten user stories
1. As a college student, I want to create an account so that my information is saved under my own profile.
2. As a returning student, I want to sign in so that I can access my dashboard.
3. As a student taking multiple courses, I want to add a course label to an assignment so that I can identify which class it belongs to.
4. As a busy student, I want to enter an assignment due date so that I can plan around deadlines.
5. As a student prioritizing work, I want to assign Low, Medium, or High priority so that I can decide what to work on first.
6. As a student, I want to mark an assignment complete so that my task list reflects my progress.
7. As a student, I want to reopen an assignment if I marked it complete by mistake so that my records stay accurate.
8. As a student, I want to set an academic goal and target date so that I can work toward a measurable outcome.
9. As a student, I want to mark a goal complete so that I can track accomplishments.
10. As a student, I want my dashboard to summarize assignments so that I can quickly understand my workload.

## Five scenarios
### Scenario 1: New student registers
A student visits the landing page, selects Get started, enters a name, valid email, and password of at least eight characters. The system creates an account and directs the student to sign in. If the email already exists, the system displays an error and does not create a duplicate.

### Scenario 2: Student signs in
A registered student enters their email and password. When credentials match, the system starts a session and opens the dashboard. When credentials do not match, the system displays a generic error and does not grant access.

### Scenario 3: Student adds an assignment
A signed-in student enters an assignment title, course, due date, and priority. The system validates required fields, saves the assignment for that user, and shows it on the dashboard. A missing title or due date is rejected with a message.

### Scenario 4: Student completes an assignment
A student selects Mark complete for an existing assignment. The system changes its status to Completed and the dashboard summary updates. The student can choose Reopen to return it to Pending.

### Scenario 5: Student sets and completes a goal
A student enters a goal and target date. The system saves the goal. The student later checks the completion control and the goal is marked complete; the student can delete the goal if it is no longer needed.

## Acceptance criteria
- Unauthenticated users cannot open the dashboard.
- Duplicate email addresses cannot register twice.
- Passwords are hashed before storage.
- A student sees only their own assignments and goals.
- Task and goal create/update/delete actions persist in SQLite.
- Invalid task status values are rejected.
- Dashboard summary counts reflect stored task statuses and dates.
