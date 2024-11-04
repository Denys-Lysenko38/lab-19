import random

# Функція додає випадковий розділовий знак до кінця кожного слова
def add_random_punctuation(text):
    punctuation = ['.', ',', '!', '?', ':', ';']
    words = text.split()
    modified_words = [word + random.choice(punctuation) for word in words]
    print(" ".join(modified_words))

# Функція виводить слова, які повторюються, у стовпчик
def print_repeated_words(text):
    words = text.split()
    unique_words = set()
    repeated_words = set()
    for word in words:
        if word in unique_words:
            repeated_words.add(word)
        else:
            unique_words.add(word)
    print("Повторювані слова:")
    for word in repeated_words:
        print(word)

# Основна програма
text = input("Введіть рядок слів, розділених пробілами: ")
add_random_punctuation(text)
print_repeated_words(text)
