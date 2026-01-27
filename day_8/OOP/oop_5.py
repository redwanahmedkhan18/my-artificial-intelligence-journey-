class student:
    def __init__(self,name,id,dept,university,semester,contact,address,country):
        self.name=name
        self.id=id
        self.dept=dept
        self.university=university
        self.semester=semester
        self.contact=contact
        self.address=address
        self.country=country
        self.course="Artificial Intelligence"

    def update_info(self,contact,address,country,semester,course,dept):
        self.contact=contact
        self.address=address
        self.country=country
        self.semester=semester
        self.course=course
        self.dept=dept


    def display_student_info(self):
        print("Student Name:",self.name)
        print("Student ID:",self.id)
        print("Department:",self.dept)
        print("University:",self.university)
        print("Semester:",self.semester)
        print("Contact:",self.contact)
        print("Address:",self.address)
        print("Country:",self.country)
        print("Course:",self.course)
        print("----------------------------------------")


s1=student("Alice Smith", "54321", "Artificial Intelligence", "Massachussetts Institute of Technology", "Fall 2026", "+1-555-1234", "123 AI Lane, Cambridge, MA", "USA")
s1.display_student_info()
s1.update_info("+1-555-5678", "456 ML Road, Cambridge, MA", "USA", "Spring 2027", "Machine Learning", "Computer Science")
s1.display_student_info()
s2=student("John Doe", "12345", "Computer Science", "Harvard University", "Fall 2026", "+1-555-8765", "789 Data St, Cambridge, MA", "USA")
s2.display_student_info()
s2.update_info("+1-555-4321", "321 Robotics Ave, Cambridge, MA", "USA", "Spring 2027", "Robotics", "Artificial Intelligence")
s2.display_student_info()

print(s1.__dict__)

print(s2.__dir__())