-- =====================================================
-- GenAI Campus ERP Assistant Database Schema
-- =====================================================

CREATE DATABASE IF NOT EXISTS campus_erp;
USE campus_erp;

-- =====================================================
-- Students
-- =====================================================

CREATE TABLE students (
student_id INT PRIMARY KEY AUTO_INCREMENT,
enrollment_no VARCHAR(20) UNIQUE NOT NULL,
first_name VARCHAR(50) NOT NULL,
last_name VARCHAR(50),
email VARCHAR(100) UNIQUE,
phone VARCHAR(15),
gender VARCHAR(10),
branch VARCHAR(50),
semester INT,
section VARCHAR(10),
cgpa DECIMAL(3,2),
admission_year INT,
status VARCHAR(20) DEFAULT 'Active'
);

-- =====================================================
-- Faculty
-- =====================================================

CREATE TABLE faculty (
faculty_id INT PRIMARY KEY AUTO_INCREMENT,
faculty_name VARCHAR(100) NOT NULL,
email VARCHAR(100),
department VARCHAR(50),
designation VARCHAR(50)
);

-- =====================================================
-- Subjects
-- =====================================================

CREATE TABLE subjects (
subject_id INT PRIMARY KEY AUTO_INCREMENT,
subject_code VARCHAR(20) UNIQUE,
subject_name VARCHAR(100),
credits INT,
semester INT,
faculty_id INT,
FOREIGN KEY (faculty_id) REFERENCES faculty(faculty_id)
);

-- =====================================================
-- Attendance
-- =====================================================

CREATE TABLE attendance (
attendance_id INT PRIMARY KEY AUTO_INCREMENT,
student_id INT,
subject_id INT,
classes_attended INT,
total_classes INT,
attendance_percentage DECIMAL(5,2),
FOREIGN KEY (student_id) REFERENCES students(student_id),
FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
);

-- =====================================================
-- Exams
-- =====================================================

CREATE TABLE exams (
exam_id INT PRIMARY KEY AUTO_INCREMENT,
subject_id INT,
exam_type VARCHAR(30),
exam_date DATE,
exam_time TIME,
room_no VARCHAR(20),
FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
);

-- =====================================================
-- Results
-- =====================================================

CREATE TABLE results (
result_id INT PRIMARY KEY AUTO_INCREMENT,
student_id INT,
subject_id INT,
marks INT,
grade VARCHAR(5),
semester INT,
FOREIGN KEY (student_id) REFERENCES students(student_id),
FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
);

-- =====================================================
-- Assignments
-- =====================================================

CREATE TABLE assignments (
assignment_id INT PRIMARY KEY AUTO_INCREMENT,
subject_id INT,
title VARCHAR(200),
description TEXT,
due_date DATE,
status VARCHAR(20),
FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
);

-- =====================================================
-- Timetable
-- =====================================================

CREATE TABLE timetable (
timetable_id INT PRIMARY KEY AUTO_INCREMENT,
subject_id INT,
day_of_week VARCHAR(20),
start_time TIME,
end_time TIME,
classroom VARCHAR(20),
FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
);

-- =====================================================
-- Fees
-- =====================================================

CREATE TABLE fees (
fee_id INT PRIMARY KEY AUTO_INCREMENT,
student_id INT,
total_fee DECIMAL(10,2),
paid_fee DECIMAL(10,2),
pending_fee DECIMAL(10,2),
due_date DATE,
status VARCHAR(20),
FOREIGN KEY (student_id) REFERENCES students(student_id)
);

-- =====================================================
-- Placement Companies
-- =====================================================

CREATE TABLE companies (
company_id INT PRIMARY KEY AUTO_INCREMENT,
company_name VARCHAR(100),
package_lpa DECIMAL(5,2),
min_cgpa DECIMAL(3,2),
eligible_branches VARCHAR(200),
application_deadline DATE
);

-- =====================================================
-- Placement Applications
-- =====================================================

CREATE TABLE applications (
application_id INT PRIMARY KEY AUTO_INCREMENT,
student_id INT,
company_id INT,
application_status VARCHAR(30),
FOREIGN KEY (student_id) REFERENCES students(student_id),
FOREIGN KEY (company_id) REFERENCES companies(company_id)
);

-- =====================================================
-- Notifications
-- =====================================================

CREATE TABLE notifications (
notification_id INT PRIMARY KEY AUTO_INCREMENT,
title VARCHAR(200),
message TEXT,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =====================================================
-- ERP Chat History (For AI Assistant)
-- =====================================================

CREATE TABLE chat_history (
chat_id INT PRIMARY KEY AUTO_INCREMENT,
student_id INT,
user_query TEXT,
ai_response TEXT,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY (student_id) REFERENCES students(student_id)
);
