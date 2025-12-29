#Nested dictionary CRUD
nested_dict ={
    "student1":{
        "Name":"Redwan Ahmed Khan",
        "Age":26,
        "Passion":"AI Engineer",
        "Goals":["PhD in AI","Researcher","Professor"],
    },
    "student2":{
        "Name":"John Doe",
        "Age":24,
        "Passion":"Data Scientist",
        "Goals":["Master's in Data Science","Industry Expert"],
    },
    "student3":{
        "Name":"Jane Smith",
        "Age":25,
        "Passion":"Software Developer",
        "Goals":["Full-stack Developer","Tech Lead"],
    }
}
# Read
print(nested_dict["student1"]["Name"])

#create

nested_dict["student_4"]={
    "Name":"Nusrat Jahan Sathi",
    "Age":26,
    "Passion":"Agronomy",
    "Goals":["PhD in Agronomy","Researcher","Professor"],
}
print(nested_dict)

#Update
nested_dict["student1"]["University"]="MIT"

print(nested_dict)

nested_dict["student2"]["Goals"].append("Data Science Influencer")  
print(nested_dict)

#Delete
if "University" in nested_dict["student1"]:
    del nested_dict["student1"]["University"]


print(nested_dict)