#!/usr/bin/env python3

import sqlite3

def setup_database():
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE users (username TEXT, password TEXT)")
    cursor.execute("INSERT INTO users VALUES ('admin', 'adminpass')")
    conn.commit()
    return conn

def vulnerable_login(conn, username, password):
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print(f"[VULNERABLE] Executing: {query}")
    try:
        cursor.execute(query)
        return cursor.fetchone()
    except Exception as e:
        print(f"[ERROR] {e}")
        return None

def safe_login(conn, username, password):
    cursor = conn.cursor()
    print(f"[SAFE] Executing parameterized query with inputs: {username}, {password}")
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    return cursor.fetchone()

def run_demo():
    print("=== SQL Injection Demo ===\n")
    conn = setup_database()

    print("1. Attempting normal login (correct credentials):")
    print("   Result:", vulnerable_login(conn, "admin", "adminpass"))

    print("\n2. Attempting SQL injection with username = \"admin' --\":")
    print("   Result:", vulnerable_login(conn, "admin' --", ""))

    print("\n3. Attempting SQL injection with username = \"' OR '1'='1\":")
    print("   Result:", vulnerable_login(conn, "' OR '1'='1", "anything"))

    print("\n4. Using safe (parameterized) login with injection inputs:")
    print("   Result:", safe_login(conn, "' OR '1'='1", "anything"))

if __name__ == "__main__":
    run_demo()
