from fastapi import FastAPI
from sqlalchemy import create_engine, text

app = FastAPI()

DATABASE_URL = "mysql+pymysql://root:Root@12345@localhost/campus_erp"

engine = create_engine(DATABASE_URL)

@app.get("/")
def home():
    return {"message": "GenAI Campus ERP Assistant"}

@app.get("/students")
def get_students():

    with engine.connect() as conn:

        result = conn.execute(
            text("SELECT * FROM students")
        )

        students = [
            dict(row._mapping)
            for row in result
        ]

        return students