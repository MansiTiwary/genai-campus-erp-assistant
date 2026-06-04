# AI Powered Campus ERP Assistant

An AI-driven Campus ERP Assistant that enables students to access academic information through natural language conversations. The system integrates Generative AI, Function Calling, RAG (Retrieval-Augmented Generation), and MySQL database connectivity to provide real-time responses for attendance, examinations, assignments, placements, and academic records.

---

## 🚀 Project Overview

Traditional ERP systems require students to navigate multiple dashboards and menus to access information. This project simplifies the process by allowing users to interact with the ERP using natural language queries.

### Example Queries

* What is my attendance percentage in DBMS?
* When is my next examination?
* Show my pending assignments.
* Am I eligible for the TCS Digital placement drive?
* What is my current CGPA?
* Who is teaching Operating Systems this semester?

---

## ✨ Key Features

### Student Management

* Student profile management
* Academic records tracking
* Semester and CGPA monitoring

### Attendance Management

* Subject-wise attendance tracking
* Attendance shortage alerts
* Attendance analytics

### Examination Management

* Exam schedules
* Subject-wise examination details
* Upcoming exam reminders

### Assignment Tracking

* Assignment submission status
* Due-date monitoring
* Pending assignment notifications

### Placement Assistance

* Company eligibility verification
* Placement opportunity tracking
* Package and criteria analysis

### AI-Powered Assistant

* Natural language interaction
* Context-aware responses
* Real-time database querying using Function Calling

### RAG-Based Knowledge Retrieval

* College policies
* Academic regulations
* Student handbook information
* Frequently asked questions

---

## 🏗️ System Architecture

Student Query

⬇

GenAI Assistant (Gemini API)

⬇

Function Calling Layer

⬇

FastAPI Backend

⬇

MySQL Database

---

## 🛠️ Technology Stack

### Backend

* Python
* FastAPI

### Database

* MySQL

### Generative AI

* Gemini API

### RAG Framework

* LangChain
* ChromaDB

### Frontend

* Streamlit

### Version Control

* Git
* GitHub

---

## 📂 Project Structure

```text
genai-campus-erp-assistant/
│
├── backend/
│   ├── app.py
│   ├── database.py
│   └── routes/
│
├── database/
│   ├── schema.sql
│   └── sample_data.sql
│
├── docs/
│   └── project_documentation.md
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🎯 Learning Outcomes

* Generative AI Application Development
* Retrieval-Augmented Generation (RAG)
* Function Calling and Tool Usage
* REST API Development
* Database Design and Integration
* Enterprise Software Architecture

---

## 🔮 Future Enhancements

* Voice-Based Campus Assistant
* Multi-Agent AI System
* Mobile Application Support
* Personalized Study Planner
* AI-Based Placement Preparation Assistant

---

## 📌 Project Status

🚧 Currently under active development.

This project is being developed as a real-world Generative AI application to demonstrate enterprise-grade AI integration with academic ERP systems.


## Copyright

© 2026 Mansi Tiwary. All Rights Reserved.

This project and its source code may not be copied, modified, distributed, or used for commercial purposes without explicit written permission from the author.
