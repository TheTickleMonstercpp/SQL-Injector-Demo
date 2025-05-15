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

def vulnerable_login_demo(conn):
    print("\n[VULNERABLE LOGIN DEMO]")
    test_cases = [
        ("Normal login (admin/adminpass)", "admin", "adminpass"),
        ("Injection attempt with username = \"admin' --\"", "admin' --", ""),
        ("Injection attempt with username = \"' OR '1'='1\"", "' OR '1'='1", "irrelevant"),
    ]
    cursor = conn.cursor()

    for desc, username, password in test_cases:
        print(f"\nTest case: {desc}")
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        print(f"Input username: {username}")
        print(f"Input password: {password}")
        print(f"Constructed SQL query:\n{query}")
        try:
            cursor.execute(query)
            result = cursor.fetchone()
            if result:
                print("Login successful (vulnerable to injection).")
            else:
                print("Login failed.")
        except Exception as e:
            print(f"Error executing query: {e}")

def safe_login_demo(conn):
    print("\n[SAFE LOGIN DEMO]")
    test_cases = [
        ("Normal login (admin/adminpass)", "admin", "adminpass"),
        ("Injection attempt with username = \"' OR '1'='1\"", "' OR '1'='1", "irrelevant"),
    ]
    cursor = conn.cursor()

    for desc, username, password in test_cases:
        print(f"\nTest case: {desc}")
        print(f"Input username: {username}")
        print(f"Input password: {password}")
        try:
            cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
            result = cursor.fetchone()
            if result:
                print("Login successful (safe method).")
            else:
                print("Login failed (injection attempt blocked).")
        except Exception as e:
            print(f"Error executing secure query: {e}")

def main_menu():
    conn = setup_database()
    print_banner()

    while True:
        print("\nPlease select an option:")
        print("1. Run vulnerable login demo")
        print("2. Run safe login demo")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            vulnerable_login_demo(conn)
        elif choice == "2":
            safe_login_demo(conn)
        elif choice == "3":
            print("Exiting. Thank you for learning about SQL injection safely!")
            break
        else:
            print("Invalid input. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main_menu()
    input("\nPress Enter to exit...")
