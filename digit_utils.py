# digit_utils.py

def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

def max_digit(number):
    return max(int(digit) for digit in str(number))

def min_digit(number):
    return min(int(digit) for digit in str(number))