USE campus_erp;

-- =====================================================
-- Insert Students
-- =====================================================
INSERT INTO students (enrollment_no, first_name, last_name, email, phone, gender, branch, semester, section, cgpa, admission_year, status) VALUES 
('CS23001', 'Alice', 'Smith', 'alice@example.com', '1234567890', 'Female', 'Computer Science', 5, 'A', 8.50, 2021, 'Active'),
('CS23002', 'Bob', 'Johnson', 'bob@example.com', '0987654321', 'Male', 'Computer Science', 5, 'A', 7.20, 2021, 'Active'),
('EE23001', 'Charlie', 'Brown', 'charlie@example.com', '1112223333', 'Male', 'Electrical Engineering', 5, 'B', 9.10, 2021, 'Active'),
('ME23001', 'Diana', 'Prince', 'diana@example.com', '4445556666', 'Female', 'Mechanical Engineering', 3, 'A', 8.80, 2022, 'Active'),
('CS23003', 'Eve', 'Adams', 'eve@example.com', '7778889999', 'Female', 'Computer Science', 5, 'B', 9.50, 2021, 'Active'),
('EC23001', 'Frank', 'Wright', 'frank@example.com', '5556667777', 'Male', 'Electronics', 1, 'C', 7.90, 2023, 'Active');

-- =====================================================
-- Insert Faculty
-- =====================================================
INSERT INTO faculty (faculty_name, email, department, designation) VALUES 
('Dr. Alan Turing', 'alan@example.com', 'Computer Science', 'Professor'),
('Dr. Nikola Tesla', 'nikola@example.com', 'Electrical Engineering', 'Associate Professor'),
('Dr. Marie Curie', 'marie@example.com', 'Mechanical Engineering', 'Assistant Professor'),
('Dr. Ada Lovelace', 'ada@example.com', 'Computer Science', 'Assistant Professor'),
('Dr. John von Neumann', 'john@example.com', 'Mathematics', 'Professor');

-- =====================================================
-- Insert Subjects
-- =====================================================
INSERT INTO subjects (subject_code, subject_name, credits, semester, faculty_id) VALUES 
('CS301', 'Data Structures', 4, 3, 1),
('CS302', 'Operating Systems', 4, 5, 4),
('EE301', 'Circuit Theory', 4, 3, 2),
('ME301', 'Thermodynamics', 4, 3, 3),
('CS303', 'Database Management', 4, 5, 1),
('MA101', 'Engineering Mathematics 1', 4, 1, 5);

-- =====================================================
-- Insert Attendance
-- =====================================================
INSERT INTO attendance (student_id, subject_id, classes_attended, total_classes, attendance_percentage) VALUES 
(1, 2, 35, 40, 87.50),
(2, 2, 30, 40, 75.00),
(1, 5, 38, 40, 95.00),
(3, 3, 36, 40, 90.00),
(4, 4, 20, 40, 50.00),
(5, 2, 39, 40, 97.50),
(6, 6, 40, 40, 100.00);

-- =====================================================
-- Insert Exams
-- =====================================================
INSERT INTO exams (subject_id, exam_type, exam_date, exam_time, room_no) VALUES 
(2, 'Midterm', '2023-10-15', '10:00:00', 'Room 101'),
(5, 'Midterm', '2023-10-16', '10:00:00', 'Room 102'),
(3, 'Final', '2023-12-10', '14:00:00', 'Room 201'),
(4, 'Midterm', '2023-10-17', '10:00:00', 'Lab 1'),
(6, 'Final', '2023-12-15', '09:00:00', 'Hall A');

-- =====================================================
-- Insert Results
-- =====================================================
INSERT INTO results (student_id, subject_id, marks, grade, semester) VALUES 
(1, 2, 85, 'A', 5),
(2, 2, 65, 'C', 5),
(1, 5, 92, 'A+', 5),
(3, 3, 78, 'B+', 5),
(5, 2, 95, 'A+', 5),
(4, 4, 88, 'A', 3);

-- =====================================================
-- Insert Assignments
-- =====================================================
INSERT INTO assignments (subject_id, title, description, due_date, status) VALUES 
(2, 'OS Scheduling', 'Implement CPU scheduling algorithms', '2023-10-01', 'Active'),
(5, 'SQL Queries', 'Write complex SQL queries for ERP', '2023-10-05', 'Active'),
(3, 'Circuit Design', 'Design a basic amplifier circuit', '2023-10-10', 'Active'),
(1, 'Binary Trees', 'Implement BST traversal', '2023-09-20', 'Closed'),
(6, 'Calculus Problem Set', 'Solve integration problems', '2023-09-25', 'Closed');

-- =====================================================
-- Insert Timetable
-- =====================================================
INSERT INTO timetable (subject_id, day_of_week, start_time, end_time, classroom) VALUES 
(2, 'Monday', '09:00:00', '10:00:00', 'Room 101'),
(5, 'Monday', '10:00:00', '11:00:00', 'Room 102'),
(3, 'Tuesday', '11:00:00', '12:00:00', 'Room 201'),
(4, 'Wednesday', '09:00:00', '11:00:00', 'Lab 1'),
(6, 'Thursday', '08:00:00', '09:30:00', 'Hall A');

-- =====================================================
-- Insert Fees
-- =====================================================
INSERT INTO fees (student_id, total_fee, paid_fee, pending_fee, due_date, status) VALUES 
(1, 50000.00, 50000.00, 0.00, '2023-08-01', 'Paid'),
(2, 50000.00, 25000.00, 25000.00, '2023-12-01', 'Partial'),
(3, 50000.00, 0.00, 50000.00, '2023-08-01', 'Pending'),
(4, 50000.00, 50000.00, 0.00, '2023-08-01', 'Paid'),
(5, 50000.00, 50000.00, 0.00, '2023-08-01', 'Paid'),
(6, 45000.00, 40000.00, 5000.00, '2023-10-15', 'Partial');

-- =====================================================
-- Insert Placement Companies
-- =====================================================
INSERT INTO companies (company_name, package_lpa, min_cgpa, eligible_branches, application_deadline) VALUES 
('Google', 25.00, 8.50, 'Computer Science', '2024-01-15'),
('TCS Digital', 7.50, 7.00, 'Computer Science, Electrical Engineering, Electronics', '2023-11-01'),
('Tesla', 15.00, 8.00, 'Electrical Engineering, Mechanical Engineering', '2023-12-15'),
('Microsoft', 22.00, 8.00, 'Computer Science', '2024-01-20'),
('Infosys', 4.50, 6.00, 'All Branches', '2023-10-30');

-- =====================================================
-- Insert Placement Applications
-- =====================================================
INSERT INTO applications (student_id, company_id, application_status) VALUES 
(1, 1, 'Applied'),
(1, 2, 'Offered'),
(2, 2, 'Applied'),
(3, 3, 'Interviewing'),
(5, 1, 'Applied'),
(5, 4, 'Interviewing'),
(4, 3, 'Applied'),
(6, 5, 'Applied');

-- =====================================================
-- Insert Notifications
-- =====================================================
INSERT INTO notifications (title, message) VALUES 
('Midterm Exams', 'Midterm exams schedule has been published in the portal.'),
('Fee Reminder', 'Please clear pending dues by Dec 1st.'),
('Placement Drive', 'TCS Digital is arriving on Nov 15th for campus placements.'),
('Holiday', 'Campus will remain closed on Oct 2nd for Gandhi Jayanti.');

-- =====================================================
-- Insert ERP Chat History
-- =====================================================
INSERT INTO chat_history (student_id, user_query, ai_response) VALUES 
(1, 'What is my attendance in OS?', 'Your attendance in Operating Systems is 87.5% (35/40 classes attended).'),
(1, 'Am I eligible for Google placement?', 'Yes, you meet the 8.5 CGPA criteria for Google (Your CGPA: 8.50).'),
(2, 'Do I have pending fees?', 'Yes, you have pending fees of Rs. 25,000 due by Dec 1st, 2023.'),
(4, 'Where is Thermodynamics midterm?', 'Thermodynamics midterm is scheduled on Oct 17, 2023 at Lab 1.');
