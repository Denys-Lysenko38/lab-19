import pandas as pd

df = pd.read_csv('masiv.csv', header=None, names=["Ім'я", "Телефон", "Місто"])
name = input("Введіть ім'я користувача: ")
result = df[df["Ім'я"] == name]
if not result.empty:
    print(result)
else:
    print("Користувач з таким іменем не знайдений.")