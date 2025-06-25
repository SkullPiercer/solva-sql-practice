import sqlite3
from pathlib import Path

import pytest

SCHEMA_PATH = Path("tasks/schema.sql")
SEED_PATH = Path("tests/seed.sql")
QUERIES_PATH = Path("tasks/queries.sql")


def extract_query_by_index(file_path: Path, index: int) -> str:
    with open(file_path, encoding="utf-8") as f:
        content = f.read()

    blocks = content.split("--")
    queries = [b.strip() for b in blocks if b.strip() and b.strip()[0].isdigit()]

    try:
        return queries[index - 1].split("\n", 1)[1].strip()
    except IndexError:
        raise ValueError(f"Запрос #{index} не найден в файле {file_path}")


def run_query(conn, query):
    cur = conn.cursor()
    cur.execute(query)
    return cur.fetchall()


@pytest.fixture(scope="function")
def db():
    conn = sqlite3.connect(":memory:")
    conn.execute("PRAGMA foreign_keys = ON;")
    with open(SCHEMA_PATH, encoding="utf-8") as f:
        conn.executescript(f.read())
    with open(SEED_PATH, encoding="utf-8") as f:
        conn.executescript(f.read())
    yield conn
    conn.close()


def test_query_01_courses_and_instructors(db):
    query = extract_query_by_index(QUERIES_PATH, 1)
    result = run_query(db, query)
    assert ("SQL Basics", "Dr. Smith") in result


def test_query_02_students_on_sql_basics(db):
    query = extract_query_by_index(QUERIES_PATH, 2)
    result = run_query(db, query)
    assert ("Alice",) in result and ("Bob",) in result


def test_query_03_alice_progress(db):
    query = extract_query_by_index(QUERIES_PATH, 3)
    result = run_query(db, query)
    assert ("SQL Basics", "SELECT Basics", 90) in result
    assert ("SQL Basics", "WHERE Conditions", 85) in result


def test_query_04_avg_score_per_course(db):
    query = extract_query_by_index(QUERIES_PATH, 4)
    result = dict(run_query(db, query))
    assert result["SQL Basics"] == 81.67


def test_query_05_students_with_no_progress(db):
    query = extract_query_by_index(QUERIES_PATH, 5)
    print(query)
    result = run_query(db, query)
    print(result)
    assert ("Charlie",) in result
