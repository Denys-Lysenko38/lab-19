import pickle

grades = {
    "Іваненко": 12,
    "Петренко": 6,
    "Сидоренко": 8,
    "Коваленко": 9,
    "Тарасенко": 12,
    "Мельник": 8,
    "Шевченко": 10,
    "Гончаренко": 12,
    "Демченко": 5,
    "Кравченко": 12
}

with open("grades.bin", "wb") as file:
    pickle.dump(grades, file)

print("Словник успішно записано у файл grades.bin.")