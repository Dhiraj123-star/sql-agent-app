from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from database import SessionLocal,engine
from schemas import QueryRequest, QueryResponse
from agent import generate_sql
from utils import is_safe_sql,clean_sql
import sqlite3

app = FastAPI(title="Simple SQLite SQL Agent")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {
        "message":"SQL Agent is running!!"
    }

@app.get("/health")
def health_check():
    try:
        # simple DB check
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return {"status":"healthy"}
    except Exception as e:
        return {"status":"unhealthy","error":str(e)}


@app.post("/query", response_model=QueryResponse)
def query_db(request: QueryRequest, db: Session = Depends(get_db)):

    # Define schema for agent
    schema = """
users (id INTEGER, name TEXT, email TEXT, role TEXT)
"""

    # Get SQL from agent
    sql = generate_sql(request.question, schema)

    # Clean SQL first
    cleaned_sql = clean_sql(sql)

    # Validate
    if not is_safe_sql(sql):
        raise HTTPException(status_code=400, detail="Only SELECT queries allowed")

    # Execute using raw sqlite3
    conn = sqlite3.connect("/data/local_data.db")
    cursor = conn.cursor()
    try:
        cursor.execute(cleaned_sql)
        columns = [desc[0]for desc in cursor.description]
        rows = cursor.fetchall()
        # Convert rows into list of dictionaries 
        result = [dict(zip(columns,row))for row in rows]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

    return {
        "sql": cleaned_sql,
        "result": result
    }