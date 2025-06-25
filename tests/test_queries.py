import sqlite3
from pathlib import Path

import pytest

BASE_DIR = Path(__file__).parent.parent
SCHEMA_PATH = BASE_DIR / "tasks/schema.sql"
SEED_PATH = BASE_DIR / "tests/seed.sql"
QUERIES_PATH = BASE_DIR / "tasks/queries.sql"

@pytest.fixture(scope="function")
def db():
    conn = sqlite3.connect(":memory:")
    conn.execute("PRAGMA foreign_keys = ON;")

    with open(SCHEMA_PATH) as f:
        conn.executescript(f.read())
    with open(SEED_PATH) as f:
        conn.executescript(f.read())
    
    yield conn

    conn.close()


def extract_queries():
    with open(QUERIES_PATH, encoding="utf-8") as f:
        content = f.read()
    queries = [q.strip() for q in content.split(";") if q.strip()]
    return queries


def test_queries_file_exists():
    assert QUERIES_PATH.exists(), "Файл queries.sql не найден"

@pytest.mark.parametrize("query_idx, expected", [
    (0, [("SQL Basics", "Dr. Smith"), ("Advanced SQL", "Dr. Smith")]),
    (1, [("Alice",), ("Bob",)]),
    (2, [("SQL Basics", "SELECT Basics", 90), ("SQL Basics", "WHERE Conditions", 85)]),
    (3, [("SQL Basics", 81.666)]),
    (4, [("Charlie",)])
])
def test_queries_results(db, query_idx, expected):
    queries = extract_queries()
    assert len(queries) >= query_idx + 1, f"Ожидается как минимум {query_idx + 1} запрос(ов)"

    cursor = db.cursor()
    cursor.execute(queries[query_idx])
    result = cursor.fetchall()

    rounded_result = [
        tuple(round(x, 2) if isinstance(x, float) else x for x in row)
        for row in result
    ]
    rounded_expected = [
        tuple(round(x, 2) if isinstance(x, float) else x for x in row)
        for row in expected
    ]

    assert sorted(rounded_result) == sorted(rounded_expected), f"Неверный результат запроса #{query_idx + 1}"
