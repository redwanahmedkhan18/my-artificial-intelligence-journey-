class Student:
    def __init__(self, name, student_id, dept, university, semester, contact, address, country):
        self.name = name
        self.student_id = student_id
        self.dept = dept
        self.university = university
        self.semester = semester
        self.contact = contact
        self.address = address
        self.country = country
        self.course = "Artificial Intelligence"
        self.tuition_fees = 0

    def set_tuition_fees(self, fees):
        self.tuition_fees = fees

    def get_tuition_fees(self):
        return self.tuition_fees


s1 = Student("Alice Smith", "54321", "Artificial Intelligence", "Massachussetts Institute of Technology", "Fall 2026", "+1-555-1234", "123 AI Lane, Cambridge, MA", "USA")  

print("Initial Tuition Fees for", s1.name, ":", s1.get_tuition_fees()   )
print("Initial Student Information:")
class Student:
    def __init__(self, name, student_id, dept, university, semester, contact, address, country):
        self.name = name
        self.student_id = student_id
        self.dept = dept
        self.university = university
        self.semester = semester
        self.contact = contact
        self.address = address
        self.country = country
        self.course = "Artificial Intelligence"
        self.tuition_fees = 0

    def set_tuition_fees(self, fees):
        self.tuition_fees = fees

    def get_tuition_fees(self):
        return self.tuition_fees
    
    def display_student_info(self):
        print("Name:", self.name)
        print("Student ID:", self.student_id)
        print("Department:", self.dept)
        print("University:", self.university)
        print("Semester:", self.semester)
        print("Contact:", self.contact)
        print("Address:", self.address)
        print("Country:", self.country)
        print("Course:", self.course)
        print("Tuition Fees:", self.tuition_fees)