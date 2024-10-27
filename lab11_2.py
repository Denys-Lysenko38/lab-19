import json

filename = "cities.json"

def load_data():
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Файл не знайдено. Створимо новий.")
        return {}
    except json.JSONDecodeError:
        print("Помилка декодування JSON. Перевірте формат файлу.")
        return {}

def save_data(data):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def show_population(city_name):
    data = load_data()
    population = data.get(city_name)
    if population:
        print(f"Населення міста {city_name}: {population}")
    else:
        print(f"Місто {city_name} не знайдено в базі даних.")

def show_all_cities():
    data = load_data()
    sorted_data = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))
    print("Список міст за спаданням кількості населення:")
    for city, population in sorted_data.items():
        print(f"{city}: {population}")

def add_city(city_name, population):
    data = load_data()
    if city_name in data:
        print(f"Місто {city_name} вже є в базі даних.")
    else:
        data[city_name] = population
        save_data(data)
        print(f"Місто {city_name} додано з населенням {population}.")

def main():
    while True:
        print("\nОберіть дію:")
        print("1. Показати населення міста")
        print("2. Показати всі міста за спаданням кількості населення")
        print("3. Додати нове місто")
        print("4. Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            city_name = input("Введіть назву міста: ")
            show_population(city_name)
        elif choice == "2":
            show_all_cities()
        elif choice == "3":
            city_name = input("Введіть назву міста: ")
            population = int(input("Введіть кількість населення: "))
            add_city(city_name, population)
        elif choice == "4":
            print("Вихід з програми.")
            break
        else:
            print("Неправильний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
