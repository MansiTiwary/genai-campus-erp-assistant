from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, text
from gemini_service import ask_gemini

app = FastAPI(title="GenAI Campus ERP Assistant")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

DATABASE_URL = "mysql+pymysql://root:Root%4012345@localhost/campus_erp"
engine = create_engine(DATABASE_URL)


@app.get("/")
def home():
    return {"message": "GenAI Campus ERP Assistant"}


@app.get("/student-list")
def get_student_list():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT DISTINCT first_name FROM students ORDER BY first_name"))
            return [row[0] for row in result]
    except Exception as e:
        return []


@app.get("/students")
def get_students():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT * FROM students"))
            return {"count": len(list(result)), "data": [dict(row._mapping) for row in conn.execute(text("SELECT * FROM students"))]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/attendance")
def get_attendance():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT * FROM attendance"))
            return [dict(row._mapping) for row in result]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/assignments")
def get_assignments():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT * FROM assignments"))
            return [dict(row._mapping) for row in result]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/exams")
def get_exams():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT * FROM exams"))
            return [dict(row._mapping) for row in result]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/companies")
def get_companies():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT * FROM companies"))
            return [dict(row._mapping) for row in result]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/ask")
def ask(body: dict):
    question = body.get("question", "")
    if not question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty")
    answer = ask_gemini(question)
    return {"question": question, "answer": answer}


@app.get("/student-cgpa")
def student_cgpa(name: str):
    try:
        with engine.connect() as conn:
            row = conn.execute(
                text("SELECT first_name, cgpa FROM students WHERE first_name = :name"),
                {"name": name}
            ).fetchone()
            if not row:
                return {"message": "Student not found"}
            prompt = f"Student Name: {row.first_name}\nCGPA: {row.cgpa}\n\nExplain the student's academic performance professionally in 2-3 sentences."
            return {"student": row.first_name, "cgpa": row.cgpa, "ai_response": ask_gemini(prompt)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/attendance-summary")
def attendance_summary(student_id: int):
    try:
        with engine.connect() as conn:
            row = conn.execute(
                text("SELECT attendance_percentage FROM attendance WHERE student_id = :id"),
                {"id": student_id}
            ).fetchone()
            if not row:
                return {"message": "Attendance record not found"}
            prompt = f"Student attendance is {row.attendance_percentage}%. Give a concise professional attendance analysis in 2-3 sentences."
            return {"attendance": row.attendance_percentage, "ai_response": ask_gemini(prompt)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/fee-status")
def fee_status(student_id: int):
    try:
        with engine.connect() as conn:
            row = conn.execute(
                text("SELECT pending_fee, status FROM fees WHERE student_id = :id"),
                {"id": student_id}
            ).fetchone()
            if not row:
                return {"message": "Fee record not found"}
            prompt = f"Pending Fee: {row.pending_fee}\nStatus: {row.status}\n\nExplain fee status professionally in 2-3 sentences."
            return {"pending_fee": float(row.pending_fee), "status": row.status, "ai_response": ask_gemini(prompt)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/placement-eligibility")
def placement_eligibility(student_id: int):
    try:
        with engine.connect() as conn:
            student = conn.execute(
                text("SELECT first_name, branch, cgpa FROM students WHERE student_id = :id"),
                {"id": student_id}
            ).fetchone()
            if not student:
                return {"message": "Student not found"}
            companies = conn.execute(text("SELECT company_name, min_cgpa FROM companies")).fetchall()
            eligible = [c.company_name for c in companies if student.cgpa >= c.min_cgpa]
            prompt = f"Student: {student.first_name}, Branch: {student.branch}, CGPA: {student.cgpa}\nEligible Companies: {', '.join(eligible) if eligible else 'None'}\n\nGive concise placement guidance in 3-4 sentences."
            return {"student": student.first_name, "cgpa": student.cgpa, "eligible_companies": eligible, "ai_response": ask_gemini(prompt)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Run with: uvicorn app:app --reload
