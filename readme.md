###### \## 📌 **Project Overview**



###### The \*\*Student Management System\*\* is a Python application designed to maintain and organize student information.  

###### It allows users to add, view, search, update, and delete student records through a \*\*menu-driven console interface\*\*.  

###### 

###### The system ensures \*\*data persistence\*\* by storing records in a `data.json` file, so all student information remains available even after the program is closed.

###### 

###### This project is a practical example of using \*\*Python data structures\*\* (lists and dictionaries), \*\*file handling\*\*, and \*\*input validation\*\* to build a real-world utility application.



###### **## 📌 Features**



###### \- ➕ \*\*Add Student\*\* – Add new records with validation (no duplicate roll numbers).  

###### \- 📖 \*\*View Students\*\* – Display all students in a formatted table.  

###### \- 🔍 \*\*Search Student\*\* – Find a student by roll number.  

###### \- ✏️ \*\*Update Student\*\* – Modify existing student details (press Enter to keep old values).  

###### \- ❌ \*\*Delete Student\*\* – Remove student records with confirmation.  

###### \- 💾 \*\*Persistence\*\* – Records are stored in `data.json` so they survive program restarts.



###### 

###### **## 🎯 Objectives**



###### \- Provide a simple and user-friendly interface to manage student records.

###### \- Demonstrate \*\*CRUD operations\*\* in Python.

###### \- Implement \*\*data persistence\*\* using JSON.

###### \- Prevent duplicate records by validating unique roll numbers.

###### \- Teach modular programming through functions and reusable code.

###### \- Lay the foundation for advanced improvements like GUI or database integration.

###### 

###### **## 🛠️ Prerequisites**



###### \- Python 3.8+

###### \- Code editor (VS Code, PyCharm, etc.)

###### \- Terminal/Command Prompt

###### 

###### **## 📂 Project Structure**



###### student-management/

###### ├─ student\_mgmt.py # Main program

###### ├─ data.json # Stores student records (auto-created)

###### ├─ README.md # Documentation

###### └─ tests/ # (Optional) Unit tests

###### └─ test\_basic.py





###### **## 📊 Data Model**



###### Each student is represented as a Python dictionary:

###### 

###### ```python

###### {

###### &nbsp; "roll\_no": "101",

###### &nbsp; "name": "Alice",

###### &nbsp; "grade": "A"

###### }

###### 

###### 

###### All student records are stored in a list:

###### 

###### students = \[]



###### **▶️ Running the Program**

###### 

###### Clone or download the project folder.

###### 

###### Open a terminal inside the project folder.

###### 

###### Run:

###### 

###### python student\_mgmt.py



###### **🖥️ Usage (Menu Options)**

###### 

###### When you run the program, you will see:

###### 

###### === Student Management System ===

###### 1\) Add Student

###### 2\) View Students

###### 3\) Search Student

###### 4\) Update Student

###### 5\) Delete Student

###### 6\) Exit

###### 

###### 

###### Choose an option by typing the corresponding number.

###### 

###### Follow the on-screen instructions to manage student records.



###### **🖼️ Screenshot**

###### 

###### 1\) Add Student

###### 2\) View Students

###### 3\) Search Student

###### 4\) Update Student

###### 5\) Delete Student

###### 6\) Exit

###### 

###### Replace screenshot.png with an actual image of your program running in the console.



###### **🧪 Testing Checklist**



###### Add → View → Verify record exists.

###### 

###### Add duplicate roll number → System rejects.

###### 

###### Search existing roll number → Found.

###### 

###### Search non-existing → Not found.

###### 

###### Update student → Can change or skip fields.

###### 

###### Delete student → Requires confirmation.

###### 

###### Exit → Data persists in data.json.



###### **🚀 Possible Improvements**



###### Search by name (partial match)

###### 

###### Sort by roll number or name

###### 

###### Export records to CSV

###### 

###### GUI (Tkinter) or Web (Flask) interface

###### 

###### Database integration (SQLite)

###### 

###### **📖 What I Learned**

###### 

###### Modeling real-world data with lists and dictionaries

###### 

###### Writing modular and reusable functions

###### 

###### File I/O handling with JSON for data persistence

###### 

###### Input validation and error handling

###### 

###### Building menu-driven console applications



###### **👨‍💻 Author**



###### Name: Charan sai reddy

###### Course/Subject: \[python]

###### Institution: \[Besent]

###### Year       : \[2025]

