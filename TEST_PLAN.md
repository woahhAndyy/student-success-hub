# Test Plan

## Scope
Tests cover public page access, registration, duplicate account rejection, login, protected dashboard access, assignment lifecycle, goal lifecycle, and user-level data isolation.

## Test cases
| ID | Test | Expected result |
|---|---|---|
| T01 | Open landing page | HTTP 200 and landing content |
| T02 | Register and sign in | Dashboard loads |
| T03 | Register same email twice | Duplicate is rejected |
| T04 | Open dashboard without session | Redirect to login |
| T05 | Add, complete, delete task | Task appears, status changes, then disappears |
| T06 | Add, toggle, delete goal | Goal appears, toggles, then disappears |
| T07 | Another account attempts deleting first user's task | First user's task remains private |

## Execution
Run `python -m unittest discover -s tests -v`. The package includes a captured test log named `TEST_RESULTS.txt`. Rerun tests in your own environment and retain the real output for the submission.

## Manual test checklist
- [ ] Register with valid details.
- [ ] Attempt duplicate email registration.
- [ ] Sign in with valid credentials.
- [ ] Attempt sign-in with incorrect password.
- [ ] Add assignment with course, due date, and each priority.
- [ ] Mark assignment complete and reopen it.
- [ ] Delete an assignment.
- [ ] Add, complete, and delete an academic goal.
- [ ] Sign out and confirm dashboard requires sign-in.
- [ ] Use two accounts and verify data is separated.
- [ ] Test layout at desktop and mobile widths.
