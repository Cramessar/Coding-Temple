#lesson3

students = {
    'Alice': 85,
    'Bob': 42,
    'Charlie': 68,
    'David': 49
}

for student, grade in students.items():
    if grade >= 50:
        print(f"{student} passed.")
    else:
        print(f"{student} failed.")