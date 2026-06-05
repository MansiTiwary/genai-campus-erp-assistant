from fastapi import FastAPI
from sqlalchemy import create_engine, text
from gemini_service import ask_gemini
app = FastAPI()

DATABASE_URL = "mysql+pymysql://root:Root%4012345@localhost/campus_erp"
engine = create_engine(DATABASE_URL)

@app.get("/")
def home():
    return {"message": "GenAI Campus ERP Assistant"}

@app.get("/students")
def get_students():

    try:
        with engine.connect() as conn:

            result = conn.execute(
                text("SELECT * FROM students")
            )

            students = [
                dict(row._mapping)
                for row in result
            ]

            return {
                "count": len(students),
                "data": students
            }

    except Exception as e:
        return {
            "error": str(e)
        }
@app.get("/attendance")
def get_attendance():

    try:
        with engine.connect() as conn:

            result = conn.execute(
                text("SELECT * FROM attendance")
            )

            attendance = [
                dict(row._mapping)
                for row in result
            ]

            return attendance

    except Exception as e:
        return {"error": str(e)}

@app.get("/assignments")
def get_assignments():

    try:
        with engine.connect() as conn:

            result = conn.execute(
                text("SELECT * FROM assignments")
            )

            assignments = [
                dict(row._mapping)
                for row in result
            ]

            return assignments

    except Exception as e:
        return {"error": str(e)}

@app.get("/exams")
def get_exams():

    try:
        with engine.connect() as conn:

            result = conn.execute(
                text("SELECT * FROM exams")
            )

            exams = [
                dict(row._mapping)
                for row in result
            ]

            return exams

    except Exception as e:
        return {"error": str(e)}

@app.get("/ask")
def ask(question: str):

    answer = ask_gemini(question)

    return {
        "question": question,
        "answer": answer
    }
@app.get("/student-cgpa")
def student_cgpa(name: str):

    with engine.connect() as conn:

        result = conn.execute(
            text(
                """
                SELECT first_name,cgpa
                FROM students
                WHERE first_name=:name
                """
            ),
            {"name": name}
        )

        row = result.fetchone()

        if not row:
            return {"message": "Student not found"}

        prompt = f"""
        Student Name: {row.first_name}
        CGPA: {row.cgpa}

        Explain the student's academic performance professionally.
        """

        answer = ask_gemini(prompt)

        return {
            "student": row.first_name,
            "cgpa": row.cgpa,
            "ai_response": answer
        }