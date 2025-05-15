# SQL Injection Demo (Educational Example)

## Overview

This project demonstrates the basics of **SQL Injection** vulnerabilities by comparing:

- A vulnerable login function that constructs SQL queries unsafely by concatenating user input.
- A secure login function that uses parameterized queries to prevent SQL injection.

It uses an **in-memory SQLite database** for safe, local demonstration purposes only.

---

## Important Notice

- This script is for **educational purposes only**.
- It is **NOT** intended for real-world exploitation, penetration testing, or attacking any live systems.
- The database is temporary and exists only while the script is running.
- Do **NOT** use the vulnerable coding patterns shown here in any production or public-facing applications.

---

## Features

- Interactive command-line interface with a simple menu.
- Demonstrates how certain malicious inputs can bypass authentication when queries are constructed unsafely.
- Shows how parameterized queries defend against such attacks.
- Easy to run and modify for learning purposes.

---

## How to Run

1. Make sure you have Python 3 installed.
2. Run the script from a terminal or command prompt:

   ```bash
   python sql_injection_demo.py
