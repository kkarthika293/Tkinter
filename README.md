# Student Details Management (Tkinter)

**Project:** Student Details Management GUI (Tkinter)

**Short description**
A simple desktop application built with **Python** and **Tkinter** to manage student details. The app provides a user-friendly GUI to **create, read, update, and delete (CRUD)** student records and connects to a database (SQLite or MySQL). It is ideal as a learning project for beginners who want to practice GUI development, database integration, and basic software structure.

---

## Features

* Add new student records (Name, Roll No, Age, Class, Email, Phone, Address)
* View a list of saved students
* Edit existing student records
* Delete student records
* Search students by name or roll number
* Connects to either **SQLite** (default, zero setup) or **MySQL** (optional)
* Simple validation for required fields

---

## Tech stack

* Python 3.8+
* Tkinter (built-in GUI library)
* SQLite3 (built-in) or MySQL (via `mysql-connector-python` or `PyMySQL`)

---

## Prerequisites

* Python 3.8 or later installed
* (Optional for MySQL) MySQL server installed and running
* (Optional for MySQL) `mysql-connector-python` or `PyMySQL` installed

Install optional packages with pip:

```bash
pip install mysql-connector-python
# or
pip install PyMySQL
```

---

## Installation & Quick Start (SQLite - recommended for beginners)

1. Clone or download the repository.
2. (Optional) Create and activate a Python virtual environment:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

3. Run the application:

```bash
python main.py
```

The app will create a local SQLite database file (e.g. `students.db`) if it does not exist.

---

## Database setup

### SQLite (default — easiest)

The app uses `sqlite3` and will create a file like `students.db`. The table schema used in the project:

```sql
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    roll_no TEXT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    age INTEGER,
    class TEXT,
    email TEXT,
    phone TEXT,
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### MySQL (optional)

1. Create a database and user in MySQL:

```sql
CREATE DATABASE student_db;
CREATE USER 'student_user'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON student_db.* TO 'student_user'@'localhost';
FLUSH PRIVILEGES;
```

2. Create the `students` table in `student_db` (same schema as above, but using `INT AUTO_INCREMENT` for id and `TIMESTAMP` for created_at).

3. Configure connection in your app (example using `mysql-connector-python`):

```python
import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='student_user',
    password='your_password',
    database='student_db'
)
cursor = conn.cursor()
```

> Note: The project includes a config file (`config.py`) where you can switch between `sqlite` and `mysql` and store DB credentials.

---

## Usage guide (what each UI screen does)

* **Home / Dashboard** — quick actions (Add Student, View All, Search)
* **Add Student** — form to enter student details and save to DB
* **View Students** — table/list showing saved students with Edit and Delete buttons
* **Edit Student** — opens the record in the same form to update values
* **Search** — search by name or roll number and display results

---

## Example code snippets

### Creating the database connection (SQLite)

```python
import sqlite3

def get_connection(sqlite_path='students.db'):
    conn = sqlite3.connect(sqlite_path)
    return conn

# Usage
conn = get_connection()
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    roll_no TEXT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    age INTEGER,
    class TEXT,
    email TEXT,
    phone TEXT,
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)''')
conn.commit()
```

### Simple insert function

```python
def add_student(conn, data):
    sql = '''INSERT INTO students (roll_no, name, age, class, email, phone, address)
             VALUES (?, ?, ?, ?, ?, ?, ?)'''
    cursor = conn.cursor()
    cursor.execute(sql, data)
    conn.commit()
```

> For MySQL parameter placeholders use `%s` instead of `?` depending on the connector.

---

## Project structure (suggested)

```
student-tkinter-app/
│
├─ main.py            # App entry point, sets up Tk root and shows dashboard
├─ gui/               # GUI related modules
│  ├─ dashboard.py
│  ├─ add_student.py
│  └─ view_students.py
├─ db/                # Database helper modules
│  ├─ connection.py   # handles switching sqlite/mysql
│  └─ student_repo.py # CRUD functions for student model
├─ config.py          # DB config and app constants
├─ requirements.txt   # optional, lists pip packages
└─ README.md
```

---

## Validation & Error handling suggestions

* Ensure `roll_no` is unique and not empty.
* Check email format (simple regex) if you need it.
* Validate phone number length (optional).
* Catch DB exceptions and show friendly messages in the UI using `messagebox`.

---

## Troubleshooting

* If the app fails to start: check Python version and that `main.py` is present.
* SQLite: ensure the application has write permission to the folder to create `students.db`.
* MySQL: confirm credentials, host, and that the MySQL server is running.

---

## Future improvements / To-do

* Add export to CSV / Excel
* Add pagination for large number of students
* Add bulk import from CSV
* Add user authentication for multiple users
* Improve UI with `ttk`/themes or custom widgets

---

## License

This project is released under the MIT License — feel free to reuse, modify, and improve it.

---

## Contact

Created by: Your Name
Email: (mailto:kkarthika2930@gmail.com)
