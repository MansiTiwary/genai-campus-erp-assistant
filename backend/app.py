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
@app.get("/attendance-summary")
def attendance_summary(student_id: int):

    with engine.connect() as conn:

        result = conn.execute(
            text("""
                SELECT attendance_percentage
                FROM attendance
                WHERE student_id=:id
            """),
            {"id": student_id}
        )

        row = result.fetchone()

        if not row:
            return {"message": "Attendance not found"}

        prompt = f"""
        Student attendance is {row.attendance_percentage}%.

        Give a professional attendance analysis.
        """

        answer = ask_gemini(prompt)

        return {
            "attendance": row.attendance_percentage,
            "ai_response": answer
        }
@app.get("/fee-status")
def fee_status(student_id: int):

    with engine.connect() as conn:

        result = conn.execute(
            text("""
                SELECT pending_fee,status
                FROM fees
                WHERE student_id=:id
            """),
            {"id": student_id}
        )

        row = result.fetchone()

        if not row:
            return {"message": "Fee record not found"}

        prompt = f"""
        Pending Fee: {row.pending_fee}
        Status: {row.status}

        Explain fee status professionally.
        """

        answer = ask_gemini(prompt)

        return {
            "pending_fee": float(row.pending_fee),
            "status": row.status,
            "ai_response": answer
        }
@app.get("/placement-eligibility")
def placement_eligibility(student_id: int):

    with engine.connect() as conn:

        student = conn.execute(
            text("""
                SELECT first_name,branch,cgpa
                FROM students
                WHERE student_id=:id
            """),
            {"id": student_id}
        ).fetchone()

        if not student:
            return {"message":"Student not found"}

        companies = conn.execute(
            text("""
                SELECT company_name,min_cgpa
                FROM companies
            """)
        ).fetchall()

        eligible = []

        for company in companies:

            if student.cgpa >= company.min_cgpa:

                eligible.append(company.company_name)

        prompt = f"""
        Student Name: {student.first_name}
        Branch: {student.branch}
        CGPA: {student.cgpa}

        Eligible Companies:
        {', '.join(eligible)}

        Give placement guidance.
        """

        answer = ask_gemini(prompt)

        return {
            "student": student.first_name,
            "cgpa": student.cgpa,
            "eligible_companies": eligible,
            "ai_response": answer
        }
# uvicorn app:app --reload

@app.get("/companies")
def companies():

    with engine.connect() as conn:

        result = conn.execute(
            text("""
            SELECT *
            FROM companies
            """)
        )

        return [
            dict(row._mapping)
            for row in result
        ]