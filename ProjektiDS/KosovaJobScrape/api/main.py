from fastapi import FastAPI
import sqlite3

app = FastAPI()

@app.get("/jobs")
def get_jobs():
    conn = sqlite3.connect("./database/jobs.db")
    cursor = conn.cursor()
    cursor.execute("SELECT title, city, link, FROM jobs")
    jobs = cursor.fetchall()
    conn.close()
    return {"jobs": jobs}
