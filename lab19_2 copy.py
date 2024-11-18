import pickle

with open("grades.bin", "rb") as file:
    loaded_grades = pickle.load(file)

excellent_students = {name: grade for name, grade in loaded_grades.items() if grade == 12}

print("Студенти-відмінники:")
for name, grade in excellent_students.items():
    print(f"{name} - {grade}")
