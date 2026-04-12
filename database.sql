-- Create Database
CREATE DATABASE student_result_system;

-- Use Database
USE student_result_system;

-- Create Courses Table (must be first due to foreign keys)
CREATE TABLE courses(
course_id INT PRIMARY KEY AUTO_INCREMENT,
course_name VARCHAR(100) NOT NULL UNIQUE,
description TEXT NOT NULL,
created_date DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Create Subjects Table
CREATE TABLE subjects(
subject_id INT PRIMARY KEY AUTO_INCREMENT,
subject_name VARCHAR(100) NOT NULL UNIQUE,
course_id INT NOT NULL,
created_date DATETIME DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY(course_id) REFERENCES courses(course_id) ON DELETE CASCADE
);

-- Create Students Table
CREATE TABLE students(
student_id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(100) NOT NULL,
email VARCHAR(100) NOT NULL UNIQUE,
mobile VARCHAR(15) NOT NULL,
password VARCHAR(100) NOT NULL CHECK(CHAR_LENGTH(password) >= 8),
course INT NOT NULL,
created_date DATETIME DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY(course) REFERENCES courses(course_id) ON DELETE RESTRICT
);

-- Create Admin Table
CREATE TABLE admin(
admin_id INT PRIMARY KEY AUTO_INCREMENT,
username VARCHAR(50) NOT NULL UNIQUE,
password VARCHAR(50) NOT NULL,
created_date DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Create Results Table
CREATE TABLE results(
result_id INT PRIMARY KEY AUTO_INCREMENT,
student_id INT NOT NULL,
subject_id INT NOT NULL,
marks INT NOT NULL CHECK(marks >= 0 AND marks <= 100),
grade VARCHAR(5) NOT NULL CHECK(grade IN ('A+', 'A', 'B+', 'B', 'C+', 'C', 'D', 'F')),
created_date DATETIME DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY(student_id) REFERENCES students(student_id) ON DELETE CASCADE,
FOREIGN KEY(subject_id) REFERENCES subjects(subject_id) ON DELETE RESTRICT,
UNIQUE KEY unique_student_subject (student_id, subject_id)
);

-- Create Notifications Table
CREATE TABLE notifications(
notification_id INT PRIMARY KEY AUTO_INCREMENT,
student_id INT NOT NULL,
message TEXT NOT NULL,
sent_date DATETIME DEFAULT CURRENT_TIMESTAMP,
status VARCHAR(20) DEFAULT 'sent' CHECK(status IN ('sent', 'read', 'archived')),
FOREIGN KEY(student_id) REFERENCES students(student_id) ON DELETE CASCADE
);

-- Insert Default Admin
INSERT INTO admin(username,password)
VALUES('admin','admin123');

-- Create Indexes for Better Query Performance
CREATE INDEX idx_student_email ON students(email);
CREATE INDEX idx_student_course ON students(course);
CREATE INDEX idx_subject_course ON subjects(course_id);
CREATE INDEX idx_result_student ON results(student_id);
CREATE INDEX idx_result_subject ON results(subject_id);
CREATE INDEX idx_notification_student ON notifications(student_id);