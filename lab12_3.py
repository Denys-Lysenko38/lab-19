import digit_utils

number = int(input("Введіть натуральне число: "))
print("Сума цифр:", digit_utils.sum_of_digits(number))
print("Найбільша цифра:", digit_utils.max_digit(number))
print("Найменша цифра:", digit_utils.min_digit(number))
