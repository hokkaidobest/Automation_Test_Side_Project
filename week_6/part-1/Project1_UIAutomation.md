# Week 6 Part 1 (Deadline: 2022/11/24 00:00)

## Assignment
You are going to test login and logout feature. You should understand the login flow first.

Create a new test file "test_web_login.py", and write automation script for the below scenario.

### Feature: Login and Logout
#### Scenario: Login and Logout Success
- **When** member login with correct email and password
- **Then** login success and there is jwt token in local storage
- **When** member logout
- **Then** logout success

#### Scenario: Login Failed with incorrect email or password
- **When** member login with incorrect email / password
- **Then** login failed with error message

#### Scenario: Login with invalid access token
- **Given** member login with correct email and password
- **And** login success and copy the jwt token
- **And** member logout
- **And** logout success
- **When** using the jwt token to access member page
- **Then** error message "Invalid Token"

---
### Requirements:
- Using PyTest **Fixture** to write login function
- Handle the secret key (email/password) by using Environment Variables and env files.