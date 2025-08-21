import json, os

DATA_FILE = "data.json"

# ---------- Load / Save ----------
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []   # if file is empty or missing

def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump(students, f, indent=2)
    print(f"💾 Data written to {os.path.abspath(DATA_FILE)}")

"""
Minimal Student Management System
Features: Add, View, Search, Update, Delete
Fields: roll_no, name, grade
"""

# ---------- In-Memory Storage ----------
students = load_data()   # Load from data.json at startup


# ---------- Utilities ----------
def _find_by_roll(roll_no):
    for s in students:
        if s["roll_no"] == roll_no:
            return s
    return None


# ---------- Core Features ----------
def add_student():
    print("\n-- Add Student --")
    roll = input("Enter Roll No: ").strip()
    if not roll:
        print(" Roll No is required.")
        return
    if _find_by_roll(roll):
        print(" Roll No already exists.")
        return

    name = input("Enter Name: ").strip()
    if not name:
        print(" Name is required.")
        return

    grade = input("Enter Grade: ").strip()
    if not grade:
        print(" Grade is required.")
        return

    students.append({"roll_no": roll, "name": name, "grade": grade})
    print(" Student added.")


def view_students():
    print("\n-- View Students --")
    if not students:
        print("No records.")
        return
    print(f"{'Roll No':<10}{'Name':<20}{'Grade':<6}")
    print("-" * 36)
    for s in students:
        print(f"{s['roll_no']:<10}{s['name']:<20}{s['grade']:<6}")


def search_student():
    print("\n-- Search Student --")
    roll = input("Enter Roll No: ").strip()
    s = _find_by_roll(roll)
    if s:
        print(f"Found: Roll={s['roll_no']}, Name={s['name']}, Grade={s['grade']}")
    else:
        print("Not found.")


def update_student():
    print("\n-- Update Student --")
    roll = input("Enter Roll No to update: ").strip()
    s = _find_by_roll(roll)
    if not s:
        print("Not found.")
        return

    new_name = input(f"Name [{s['name']}]: ").strip()
    if new_name:
        s['name'] = new_name

    new_grade = input(f"Grade [{s['grade']}]: ").strip()
    if new_grade:
        s['grade'] = new_grade

    print("Updated.")


def delete_student():
    print("\n-- Delete Student --")
    roll = input("Enter Roll No to delete: ").strip()
    s = _find_by_roll(roll)
    if not s:
        print("Not found.")
        return
    confirm = input(f"Are you sure you want to delete {s['name']} (Roll {s['roll_no']})? (y/N): ").strip().lower()
    if confirm == "y":
        students.remove(s)
        print(" Deleted.")
    else:
        print("Cancelled.")


# ---------- Menu ----------
def main():
    while True:
        print("\n=== Student Management System ===")
        print("1) Add Student")
        print("2) View Students")
        print("3) Search Student")
        print("4) Update Student")
        print("5) Delete Student")
        print("6) Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            save_data()   # Save before exit
            print(" Data saved. Goodbye!")
            break
        else:
            print(" Invalid choice. Try again.")


if __name__ == "__main__":
    main()
