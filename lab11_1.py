import csv

with open("article.txt", "r") as file:
    text = file.read().lower()
keywords = input("Введіть 3-4 ключові слова через пробіл: ").lower().split()

keyword_counts = {word: text.count(word) for word in keywords}

with open("number.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Ключове слово", "Кількість"])
    for word, count in keyword_counts.items():
        writer.writerow([word, count])

print("Кількість ключових слів збережено у файл number.csv")