import pickle
import random
import string

L = int(input("Введіть довжину списку L: "))
N = int(input("Введіть кількість символів в одному елементі списку N: "))

random_list = [''.join(random.choices(string.ascii_letters, k=N)) for _ in range(L)]

with open("list.bin", "wb") as file:
    pickle.dump(random_list, file)

print("Список успішно записано у файл list.bin.")
