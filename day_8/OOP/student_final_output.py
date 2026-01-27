import student

s1=student.Student("Alice Smith", "54321", "Artificial Intelligence", "Massachussetts Institute of Technology", "Fall 2026", "+1-555-1234", "123 AI Lane, Cambridge, MA", "USA")
print("Initial Student Information:")
print("Initial Tuition Fees for", s1.name, ":", s1.get_tuition_fees())
s1.display_student_info()
print("\nUpdating Tuition Fees...\n")

s1.set_tuition_fees(50000)
print("Updated Tuition Fees for", s1.name, ":", s1.get_tuition_fees())
print("Updated Student Information:")
s1.display_student_info()