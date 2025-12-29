import sys
import json
import os

#File to store student data

student_file="students_data.json"

# Assign letter grade based on total weighted marks
def assign_overall_grade(weighted_marks):
    if weighted_marks >= 90:
        return "A+"
    elif weighted_marks >= 87:
        return "B+"
    elif weighted_marks >= 84:
        return "B"
    elif weighted_marks >= 81:
        return "B-"
    elif weighted_marks >= 78:
        return "C+"
    elif weighted_marks >= 75:
        return "C"
    elif weighted_marks >= 70:
        return "C-"
    elif weighted_marks >= 67:
        return "D+"
    elif weighted_marks >= 63:
        return "D"
    elif weighted_marks >= 60:
        return "D-"
    else:
        return "F"

# Map letter grade to grade points (4.0 scale)
def get_grade_points(grade):
    mapping = {
        "A+": 4.0,
        "B+": 3.75,
        "B": 3.40,
        "B-": 3.1,
        "C+": 2.8,
        "C": 2.5,
        "C-": 2.1,
        "D+": 1.8,
        "D": 1.5,
        "D-": 1.0,
        "F": 0.0
    }
    return mapping.get(grade, 0.0)

# Assign grade for individual components (optional, kept for display)
def assign_component_grade(mark):
    if mark >= 90:
        return "A+"
    elif mark >= 87:
        return "B+"
    elif mark >= 84:
        return "B"
    elif mark >= 81:
        return "B-"
    elif mark >= 78:
        return "C+"
    elif mark >= 75:
        return "C"
    elif mark >= 70:
        return "C-"
    elif mark >= 67:
        return "D+"
    elif mark >= 63:
        return "D"
    elif mark >= 60:
        return "D-"
    else:
        return "F"

# Calculate weighted total marks and GPA
def calculate_weighted_and_gpa(marks):
    weighted_total = (
        marks.get("first_term", 0) * 0.20 +
        marks.get("midterm", 0) * 0.20 +
        marks.get("attendance", 0) * 0.05 +
        marks.get("assignment", 0) * 0.05 +
        marks.get("quiz", 0) * 0.10 +
        marks.get("final_exam", 0) * 0.40
    )
    weighted_total = round(weighted_total, 2)
    overall_grade = assign_overall_grade(weighted_total)
    gpa = get_grade_points(overall_grade)
    return weighted_total, overall_grade, gpa

# Load students from JSON file
def load_students():
    if os.path.exists(student_file):
        with open(student_file, "r") as f:
            try:
                data = json.load(f)
                print(f"Loaded {len(data)} students from file.")
                return data
            except json.JSONDecodeError:
                print("Data file is empty or corrupted. Starting fresh.")
                return {}
    return {}


# Save students to JSON file
def save_students(students):
    with open(student_file, "w") as f:
        json.dump(students, f, indent=4)
    print("Student data saved to file.")

    
# Add a new student
def add_student(students, student_id, name, marks):
    if student_id in students:
        print("Student ID already exists. Use a unique ID.")
        return students

    # Validate marks range
    for key, score in marks.items():
        if not (0 <= score <= 100):
            print(f"Invalid marks for {key}: {score}. Marks must be between 0 and 100.")
            return students

    weighted, overall_grade, gpa = calculate_weighted_and_gpa(marks)
    component_grades = {subject: assign_component_grade(score) for subject, score in marks.items()}

    students[student_id] = {
        "name": name,
        "marks": marks,
        "component_grades": component_grades,
        "weighted_marks": weighted,
        "overall_grade": overall_grade,
        "gpa": gpa
    }
    print(f"New student '{name}' added successfully.")
    return students

# Update student marks
def update_marks(students, student_id, new_marks):
    if student_id not in students:
        print("Invalid Student ID. No such student found.")
        return students

    # Validate marks range
    for key, score in new_marks.items():
        if not (0 <= score <= 100):
            print(f"Invalid marks for {key}: {score}. Marks must be between 0 and 100.")
            return students

    weighted, overall_grade, gpa = calculate_weighted_and_gpa(new_marks)
    component_grades = {subject: assign_component_grade(score) for subject, score in new_marks.items()}

    students[student_id].update({
        "marks": new_marks,
        "component_grades": component_grades,
        "weighted_marks": weighted,
        "overall_grade": overall_grade,
        "gpa": gpa
    })
    print(f"Marks of Student ID {student_id} updated successfully.")
    return students

# Delete a student
def delete_student(students, student_id):
    if student_id in students:
        del students[student_id]
        print(f"Student ID {student_id} deleted successfully.")
    else:
        print("Invalid Student ID. No such student found.")
    return students

# Search for a student
def search_student(students, student_id):
    if student_id not in students:
        print("Invalid Student ID. No such student found.")
        return students

    info = students[student_id]
    print(f"\nStudent ID: {student_id}")
    print(f"Name: {info['name']}")
    print(f"Marks: {info['marks']}")
    print(f"Component Grades: {info['component_grades']}")
    print(f"Weighted Total Marks: {info['weighted_marks']}")
    print(f"Overall Grade: {info['overall_grade']}")
    print(f"GPA: {info['gpa']:.2f}")
    print("-" * 40)
    return students

# View all students
def view_all_students(students):
    if not students:
        print("No student records found.")
        return students

    for student_id, info in students.items():
        print(f"\nStudent ID: {student_id}")
        print(f"Name: {info['name']}")
        print(f"Marks: {info['marks']}")
        print(f"Component Grades: {info['component_grades']}")
        print(f"Weighted Total: {info['weighted_marks']}")
        print(f"Overall Grade: {info['overall_grade']}")
        print(f"GPA: {info['gpa']:.2f}")
        print("-" * 40)
    return students

# Calculate overall course average (weighted marks across all students)
def calculate_average_marks(students):
    if not students:
        print("No student records found.")
        return

    total_weighted = sum(info["weighted_marks"] for info in students.values())
    count = len(students)
    course_average = total_weighted / count

    print("Course Average (Weighted Marks):")
    print(f"Average Weighted Marks: {course_average:.2f}")
    print("-" * 40)

# Rank students by weighted marks (descending)
def rank_students(students):
    if not students:
        print("No student records found.")
        return students

    ranked = sorted(
        students.items(),
        key=lambda item: item[1]["weighted_marks"],
        reverse=True
    )

    print("Student Rankings (by Weighted Marks):")
    for rank, (student_id, info) in enumerate(ranked, start=1):
        print(f"Rank {rank}: ID {student_id} | {info['name']} | "
              f"Weighted: {info['weighted_marks']} | Grade: {info['overall_grade']} | GPA: {info['gpa']:.2f}")
    print("-" * 60)
    return students

# Menu-driven CLI
def main():
    students = {}
    components = ["first_term", "midterm", "attendance", "assignment", "quiz", "final_exam"]

    while True:
        print("\n===== Student Result Management System =====")
        print("1. Add Student")
        print("2. Update Student Marks")
        print("3. Delete Student")
        print("4. Search Student by ID")
        print("5. View All Students")
        print("6. Calculate Course Average")
        print("7. Rank Students")
        print("0. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            student_id = input("Enter Student ID: ").strip()
            name = input("Enter Name: ").strip()
            marks = {}
            print("Enter marks (0-100):")
            for key in components:
                while True:
                    try:
                        value = float(input(f"  {key.replace('_', ' ').title()}: "))
                        marks[key] = value
                        break
                    except ValueError:
                        print("Invalid input. Please enter a number.")
            students = add_student(students, student_id, name, marks)

        elif choice == "2":
            student_id = input("Enter Student ID to update: ").strip()
            new_marks = {}
            print("Enter new marks (0-100):")
            for key in components:
                while True:
                    try:
                        value = float(input(f"  {key.replace('_', ' ').title()}: "))
                        new_marks[key] = value
                        break
                    except ValueError:
                        print("Invalid input. Please enter a number.")
            students = update_marks(students, student_id, new_marks)

        elif choice == "3":
            student_id = input("Enter Student ID to delete: ").strip()
            students = delete_student(students, student_id)

        elif choice == "4":
            student_id = input("Enter Student ID to search: ").strip()
            students = search_student(students, student_id)

        elif choice == "5":
            view_all_students(students)

        elif choice == "6":
            calculate_average_marks(students)

        elif choice == "7":
            rank_students(students)

        elif choice == "0":
            print("Exiting Student Result Management System. Goodbye!")
            sys.exit()

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()