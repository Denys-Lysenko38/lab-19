import string

# Відкриваємо файли для читання і запису
with open("input.txt", "r") as infile, open("digit.txt", "w") as digit_file, open("symbols.txt", "w") as symbols_file:
    # Зчитуємо вміст файлу пострічно
    for line in infile:
        for char in line:
            if char.isdigit():
                digit_file.write(char)
            elif char.isalpha():  # Перевірка, чи символ є літерою
                symbols_file.write(char)
