def get_top_students(students, min_marks):
    top_students = []
    unique_courses = set()

    for student in students:
        if student['marks'] >= min_marks:
            top_students.append(student['name'])
            unique_courses.add(student['course'])

    return top_students, unique_courses

students = [    
    {"name": "Pranav", "marks": 89, "course": "Math"},
    {"name": "Neenu", "marks": 92, "course": "Science"},
    {"name": "Vishnu", "marks": 77, "course": "Social Studies"},
    {"name": "Dhanya", "marks": 89, "course": "Science"},
    {"name": "Renu", "marks": 66, "course": "Malayalam"}
] 

min_marks = 80
top_students, unique_courses = get_top_students(students, min_marks)
print("Top Students:", top_students)
print("Unique Courses:", unique_courses)