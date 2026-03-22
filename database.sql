-- Create Database
CREATE DATABASE student_result_system;

-- Use Database
USE student_result_system;

-- Create Students Table
CREATE TABLE students(
student_id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(100),
email VARCHAR(100),
mobile VARCHAR(15),
password VARCHAR(100),
course VARCHAR(50)
);

-- Create Admin Table
CREATE TABLE admin(
admin_id INT PRIMARY KEY AUTO_INCREMENT,
username VARCHAR(50),
password VARCHAR(50)
);

INSERT INTO admin(username,password)
VALUES('admin','admin123');

-- Create Results Table
CREATE TABLE results(
result_id INT PRIMARY KEY AUTO_INCREMENT,
student_id INT,
subject VARCHAR(50),
marks INT,
grade VARCHAR(5),
FOREIGN KEY(student_id) REFERENCES students(student_id)
);