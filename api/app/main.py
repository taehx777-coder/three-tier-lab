import os
import psycopg2
from fastapi import FastAPI

app = FastAPI()

DB_URL = os.getenv("DATABASE_URL", "postgresql://appuser:apppass@db:5432/appdb")

def get_conn():
    return psycopg2.connect(DB_URL)

@app.get("/health")
def health():
    try:
        with get_conn() as conn, conn.cursor() as cur:
            cur.execute("SELECT 1")
            cur.fetchone()
        return {"status": "ok"}
    except Exception as e:
        return {"status": "error", "detail": str(e)}

@app.get("/items")
def list_items():
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute("SELECT id, name FROM items ORDER BY id")
        rows = cur.fetchall()
    return [{"id": r[0], "name": r[1]} for r in rows]

