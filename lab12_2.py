import random

def generate_serial_number():
    series = random.choice(['A', 'E', 'U', 'F', 'Q', 'R', 'Z', 'W'])
    digits = ''.join([str(random.randint(0, 9)) for _ in range(8)])
    voltage = random.choice(['3', '6', '12'])
    return f"{series}{digits}-{voltage}"

n = int(input("Введіть кількість серійних номерів для генерації: "))
serial_numbers = [generate_serial_number() for _ in range(n)]
serial_numbers.sort()  # Сортуємо номери у порядку зростання

with open("serial_numbers.txt", "w") as file:
    for serial in serial_numbers:
        file.write(serial + "\n")
