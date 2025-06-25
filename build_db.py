import sqlite3


def build_db():
    conn = sqlite3.connect("db.sqlite3")
    cur = conn.cursor()

    with open("tasks/schema.sql", "r", encoding="utf-8") as f:
        cur.executescript(f.read())

    with open("tests/seed.sql", "r", encoding="utf-8") as f:
        cur.executescript(f.read())

    conn.commit()
    conn.close()
    print("База данных создана: db.sqlite3")


if __name__ == "__main__":
    build_db()
