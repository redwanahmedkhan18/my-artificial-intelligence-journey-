class University:
    def __init__(self, university_name, **kwargs):
        self.university_name = university_name
        super().__init__(**kwargs)

    def show_details(self):
        print(f"University Name: {self.university_name}")


class Course(University):
    def __init__(self, course_name, **kwargs):
        self.course_name = course_name
        super().__init__(**kwargs)

    def show_details(self):
        super().show_details()
        print(f"Course: {self.course_name}")


class Branch(University):
    def __init__(self, branch_name, **kwargs):
        self.branch_name = branch_name
        super().__init__(**kwargs)

    def show_details(self):
        super().show_details()
        print(f"Branch: {self.branch_name}")


class Student(Course, Branch):
    def __init__(self, university_name, course_name, branch_name,
                 name, student_id, dept, semester):

        self.name = name
        self.student_id = student_id
        self.dept = dept
        self.semester = semester

        super().__init__(
            university_name=university_name,
            course_name=course_name,
            branch_name=branch_name
        )

    def show_details(self):
        print("\n----- Student Details -----")
        print(f"Name: {self.name}")
        print(f"ID: {self.student_id}")
        print(f"Department: {self.dept}")
        print(f"Semester: {self.semester}")

        print("\n----- Academic Details -----")
        super().show_details()

s1 = Student(
    "MIT",
    "Artificial Intelligence",
    "Computer Science",
    "Redwan Ahmed Khan",
    26103453,
    "CSE",
    "6th"
)

s1.show_details()

