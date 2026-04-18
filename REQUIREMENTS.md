# Student Result Alert System - Requirements Gathering Document

## 1. Project Overview

**Project Name:** Student Result Alert System

**Description:** A web-based application for managing student academic records and sending automated email notifications when results are published. The system enables administrators to manage courses, subjects, and student results while allowing students to view their academic performance.

**Client/Stakeholders:** Educational Institution Administration

**Project Scope:** Desktop/Web application for academic result management and notification system

---

## 2. Functional Requirements

### 2.1 User Authentication

- **Req-F-1.1:** Student Login
  - Students must authenticate using Student ID and password
  - Password must be at least 8 characters
  - Failed login attempts should display error message
  - System should redirect to student dashboard upon successful login

- **Req-F-1.2:** Admin Login
  - Admin users authenticate with username and password
  - Must redirect to admin dashboard upon successful authentication
  - Should display error message on invalid credentials

### 2.2 Student Features

- **Req-F-2.1:** View Results
  - Students can view their academic results after login
  - Display student name, enrolled course, and results
  - Results should show: Subject Name, Marks, and Grade
  - System should allow students to view their profile information

- **Req-F-2.2:** Result Notifications
  - Students receive email notifications when results are published
  - Email should contain: Student name, subject name, marks, grade, and publication date
  - Notifications should be logged in the system

### 2.3 Admin Features

- **Req-F-3.1:** Manage Courses
  - Admin can create, read, update, and delete courses
  - Each course should have: Course ID, Course Name, and Description
  - Admin can view all courses in a table format
  - Duplicate course names should be prevented (unique constraint)

- **Req-F-3.2:** Manage Subjects
  - Admin can create, read, update, and delete subjects
  - Each subject should be associated with a course
  - Display list of all subjects with their associated courses
  - Prevent duplicate subject names

- **Req-F-3.3:** Manage Students
  - Admin can add new students to the system
  - Student information includes: Name, Email, Student ID, Mobile, Password, Course
  - Admin can view list of all enrolled students
  - Admin can edit student information
  - Admin can delete students from the system
  - Each student must have a unique email

- **Req-F-3.4:** Upload Results
  - Admin can upload results for multiple students
  - Upload should support single or bulk result entry
  - Results consist of: Student ID, Subject, Marks (0-100), Grade (A+, A, B+, B, C+, C, D, F)
  - System should validate marks are within 0-100 range
  - System should validate grade values from predefined list
  - Prevent duplicate results for same student-subject combination

- **Req-F-3.5:** Send Notifications
  - Admin can trigger email notifications to students about their results
  - Emails should be sent to student's registered email address
  - Email should contain formatted result information
  - System should track notification status (sent, read, archived)
  - Notifications should be logged in the database

- **Req-F-3.6:** View Dashboard
  - Admin dashboard should display system statistics
  - Show total number of courses, subjects, students
  - Show recent result uploads
  - Provide quick access to all management features

### 2.4 Email Notification System

- **Req-F-4.1:** Email Configuration
  - System must support SMTP for sending emails
  - Configurable email sender address
  - Should handle email delivery failures gracefully

- **Req-F-4.2:** Email Template
  - Professional email format with institution name/logo
  - Clear subject line indicating result publication
  - Student details and result breakdown
  - Academic advice or reference links

---

## 3. Non-Functional Requirements

### 3.1 Performance

- **Req-NF-1.1:** Response Time
  - Page load time should not exceed 3 seconds under normal conditions
  - Database queries should be optimized with appropriate indexes
  - Bulk email notifications should complete within reasonable timeframe

- **Req-NF-1.2:** Scalability
  - System should handle up to 5000+ students without performance degradation
  - Database should be properly indexed for frequently queried columns
  - Email queue system should handle batch operations

### 3.2 Security

- **Req-NF-2.1:** Password Security
  - Passwords must be encrypted/hashed before storage
  - Minimum password length of 8 characters enforced
  - Passwords should not be displayed in plain text

- **Req-NF-2.2:** Session Management
  - User sessions should have timeout mechanisms
  - Admin and student sessions must be separate
  - Proper logout functionality to clear sessions

- **Req-NF-2.3:** Data Protection
  - Sensitive data (email, marks, grades) must be protected
  - Database connections must use secure credentials
  - SQL injection attacks must be prevented (use parameterized queries)

- **Req-NF-2.4:** Access Control
  - Students can only view their own results
  - Admin panel restricted to authorized admin users
  - Role-based access control for different features

### 3.3 Usability

- **Req-NF-3.1:** User Interface
  - Clean, intuitive navigation across all pages
  - Responsive design for different screen sizes
  - Consistent styling and branding throughout application
  - Clear labeling and instructions for all forms

- **Req-NF-3.2:** Error Handling
  - User-friendly error messages
  - Validation feedback on form submissions
  - Proper error logging for debugging

### 3.4 Maintainability

- **Req-NF-4.1:** Code Quality
  - Code should be well-documented with comments
  - Modular design for easy updates and maintenance
  - Consistent naming conventions

- **Req-NF-4.2:** Database Design
  - Properly normalized database schema
  - Foreign key constraints to maintain data integrity
  - Indexes on frequently queried columns

### 3.5 Reliability

- **Req-NF-5.1:** Data Integrity
  - Database constraints to prevent invalid data entry
  - Backup and recovery mechanisms
  - Transaction management for critical operations

- **Req-NF-5.2:** Availability
  - System should be accessible 24/7 (after deployment)
  - Graceful handling of database connection failures

---

## 4. User Roles and Use Cases

### 4.1 Student Role

| Use Case | Description |
|----------|-------------|
| UC-1: Login | Student logs into the system with credentials |
| UC-2: View Results | Student views their grades and marks |
| UC-3: Receive Notifications | Student receives email about result publication |
| UC-4: View Profile | Student views their profile information |

### 4.2 Admin Role

| Use Case | Description |
|----------|-------------|
| UC-5: Manage Courses | Admin creates, updates, views, deletes courses |
| UC-6: Manage Subjects | Admin creates, updates, views, deletes subjects |
| UC-7: Manage Students | Admin adds, edits, views, deletes students |
| UC-8: Upload Results | Admin uploads results for students |
| UC-9: Send Notifications | Admin triggers email notifications to students |
| UC-10: View Dashboard | Admin views system statistics and summaries |

---

## 5. Technology Stack

| Component | Technology |
|-----------|-----------|
| Frontend | HTML5, CSS3, JavaScript |
| Backend Framework | Python Flask |
| Database | MySQL |
| Email Service | Python smtplib (SMTP) |
| Version Control | Git, GitHub |
| Server | Flask development/production server |

---

## 6. Database Requirements

### 6.1 Database Schema

**Tables:**
1. **courses** - Course information
2. **subjects** - Subject details linked to courses
3. **students** - Student profile and enrollment info
4. **admin** - Administrator accounts
5. **results** - Student grade records
6. **notifications** - Email notification logs

### 6.2 Data Constraints

- Student ID: Primary Key, Auto-incremented
- Email: Unique, Not Null
- Password: Minimum 8 characters
- Marks: Range 0-100
- Grade: Predefined values (A+, A, B+, B, C+, C, D, F)
- Foreign key relationships to maintain referential integrity
- Unique constraint on student-subject combination for results

### 6.3 Database Indexes

- Email index on students table for fast lookups
- Course index on students table for filtering
- Course index on subjects table
- Student index on results table for retrieving student marks
- Subject index on results table
- Student index on notifications table

---

## 7. System Routes/API Endpoints

| Route | Method | Description | Authentication |
|-------|--------|-------------|-----------------|
| / | GET | Home page (login page) | None |
| /student_login | POST | Submit student login | None |
| /student_dashboard/<student_id> | GET | View student dashboard | Student |
| /admin | GET | Admin login page | None |
| /admin_dashboard | GET | Admin dashboard | Admin |
| /manage_courses | GET | View courses management | Admin |
| /add_course | POST | Add new course | Admin |
| /manage_subjects | GET | View subjects management | Admin |
| /add_subject | POST | Add new subject | Admin |
| /add_student | GET/POST | Add student form and submission | Admin |
| /upload_result | GET/POST | Upload results form and submission | Admin |
| /view_result_page | GET | View specific result details | Student |
| /manage_students | GET | View all students | Admin |
| /send_notification | POST | Send email notifications | Admin |
| /logout | POST | User logout | All |

---

## 8. Security Requirements

### 8.1 Authentication & Authorization

- [ ] Implement secure password hashing (bcrypt/argon2)
- [ ] Session-based authentication with timeout
- [ ] CSRF protection on forms
- [ ] Rate limiting on login attempts

### 8.2 Data Security

- [ ] Use parameterized queries to prevent SQL injection
- [ ] Sanitize user inputs on frontend and backend
- [ ] Secure database credentials (environment variables, .env file)
- [ ] HTTPS for production deployment

### 8.3 Access Control

- [ ] Students can only access their own data
- [ ] Admin functions restricted to authorized admins
- [ ] View-level permissions enforcement

---

## 9. Testing Requirements

### 9.1 Unit Testing

- Test database query functions
- Test email notification logic
- Test password validation
- Test grade calculation

### 9.2 Integration Testing

- Test login workflow end-to-end
- Test result upload and notification flow
- Test database transactions

### 9.3 User Acceptance Testing

- Student login and result viewing
- Admin course/subject management
- Result upload and email notification
- Error handling scenarios

### 9.4 Performance Testing

- Load testing with multiple concurrent users
- Database query performance testing
- Email batch sending performance

---

## 10. Constraints and Assumptions

### 10.1 Constraints

- Single institution deployment (not multi-tenant yet)
- Manual email configuration required
- No real-time notifications (batch email system)
- Internet connectivity required for email functionality
- Database must be running for system operation

### 10.2 Assumptions

- All students have valid email addresses registered
- Admin users are trusted (limited administrative controls)
- MySQL database is available and configured
- SMTP server credentials are provided for email
- Students know their login credentials
- Browser supports JavaScript
- Courses and subjects are created before adding students

