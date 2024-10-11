# Програма для обробки одного рядка
def process_single_string(s):
    digits = [int(ch) for ch in s if ch.isdigit()]
    
    if digits:
        suma = sum(digits)
        product = 1
        for d in digits:
            product *= d
        return suma, product
    else:
        return 0, 0

# Введення рядка
s = input("Введіть рядок символів: ")

# Обчислення суми та добутку цифр
suma, product = process_single_string(s)
print(f"Сума цифр: {suma}")
print(f"Добуток цифр: {product}")
