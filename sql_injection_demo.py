#!/usr/bin/env python3

import sqlite3

def print_banner():
    print("=" * 60)
    print("SQL Injection Demonstration (Educational Use Only)")
    print("This script compares vulnerable and secure login methods.")
    print("=" * 60)

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
    print("\n[VULNERABLE] Attempting login...")
    print(f"Input username: {username}")
    print(f"Input password: {password}")
    print(f"Generated SQL query:\n{query}")
    try:
        cursor.execute(query)
        result = cursor.fetchone()
        if result:
            print("Login successful (vulnerable to injection).")
        else:
            print("Login failed.")
        return result
    except Exception as e:
        print(f"Error executing query: {e}")
        return None

def safe_login(conn, username, password):
    cursor = conn.cursor()
    print("\n[SAFE] Attempting login with parameterized query...")
    print(f"Input username: {username}")
    print(f"Input password: {password}")
    try:
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        result = cursor.fetchone()
        if result:
            print("Login successful (safe method).")
        else:
            print("Login failed (injection attempt blocked).")
        return result
    except Exception as e:
        print(f"Error executing secure query: {e}")
        return None

def run_demo():
    print_banner()
    conn = setup_database()

    print("\n--- Test 1: Normal Login with Correct Credentials ---")
    vulnerable_login(conn, "admin", "adminpass")

    print("\n--- Test 2: SQL Injection - Username: admin' -- ---")
    vulnerable_login(conn, "admin' --", "")

    print("\n--- Test 3: SQL Injection - Username: ' OR '1'='1 ---")
    vulnerable_login(conn, "' OR '1'='1", "irrelevant")

    print("\n--- Test 4: Secure Login with Injection Input ---")
    safe_login(conn, "' OR '1'='1", "irrelevant")

if __name__ == "__main__":
    run_demo()

