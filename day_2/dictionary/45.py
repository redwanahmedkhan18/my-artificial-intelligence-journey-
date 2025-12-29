#Student grade management system

grades={
    "student_1":{
        "id":"25203001",
        "name":"Redwan Ahmed Khan",
        "Marks":{
            "Machine Learning":95,
            "Data Science":90,
            "Artificial Intelligence":92,
            "Deep Learning":92,
            "Statistics":93,
            "Linear Algebra":89,
            "Calculus":88,
            "Python Programming":94,
            "Data Structures":91,
            "Algorithms":90

        },
        "grades":{
            "Machine Learning":"A+",
            "Data Science":"A",
            "Artificial Intelligence":"A+",
            "Deep Learning":"A+",
            "Statistics":"A",
            "Linear Algebra":"A-",
            "Calculus":"B+",
            "Python Programming":"A+",
            "Data Structures":"A",
            "Algorithms":"A"
        },
        "CGPA":3.9
    },
    "student_2":{
        "id":"25203002",
        "name":"John Doe",
        "Marks":{
            "Machine Learning":85,
            "Data Science":80,
            "Artificial Intelligence":82,
            "Deep Learning":78,
            "Statistics":83,
            "Linear Algebra":79,
            "Calculus":88,
            "Python Programming":84,
            "Data Structures":81,
            "Algorithms":80

        },
        "grades":{
            "Machine Learning":"A",
            "Data Science":"B+",
            "Artificial Intelligence":"A-",
            "Deep Learning":"B",
            "Statistics":"A-",
            "Linear Algebra":"B+",
            "Calculus":"B+",
            "Python Programming":"A",
            "Data Structures":"A-",
            "Algorithms":"B+"
        },
        "CGPA":3.4
    },
    "student_3":{
        "id":"25203003",
        "name":"Jane Smith",
        "Marks":{
            "Machine Learning":75,
            "Data Science":70,
            "Artificial Intelligence":72,
            "Deep Learning":68,
            "Statistics":73,
            "Linear Algebra":69,
            "Calculus":78,
            "Python Programming":74,
            "Data Structures":71,
            "Algorithms":70

        },
        "grades":{
            "Machine Learning":"B+",
            "Data Science":"B",
            "Artificial Intelligence":"B+",
            "Deep Learning":"C+",
            "Statistics":"B",
            "Linear Algebra":"B+",
            "Calculus":"C+",
            "Python Programming":"B+",
            "Data Structures":"B",
            "Algorithms":"B"
        },
        "CGPA":2.9
    }

}

#Add a new student
grades["student_4"]={
    "id":"25203004",
    "name":"Nusrat Jahan Sathi",
    "Marks":{
        "Machine Learning":88,
        "Data Science":92,
        "Artificial Intelligence":85,
        "Deep Learning":90,
        "Statistics":87,
        "Linear Algebra":91,
        "Calculus":89,
        "Python Programming":93,
        "Data Structures":90,
        "Algorithms":88
    },
    "grades":{
        "Machine Learning":"A",
        "Data Science":"A",
        "Artificial Intelligence":"A-",
        "Deep Learning":"A",
        "Statistics":"A-",
        "Linear Algebra":"A",
        "Calculus":"B+",
        "Python Programming":"A+",
        "Data Structures":"A",
        "Algorithms":"A"
    },
    "CGPA":3.6
}

for student, info in grades.items():
    print(f"Student: {info['name']}, CGPA: {info['CGPA']}")
    for subject, mark in info["Marks"].items():
        print(f"  {subject}: {mark}")
    print()
#Update a student's grade
grades["student_2"]["grades"]["Data Science"]="A-"
grades["student_2"]["CGPA"]=3.6 
print(f"Updated CGPA of {grades['student_2']['name']}: {grades['student_2']['CGPA']}")
