import pickle

with open("list.bin", "rb") as file:
    loaded_list = pickle.load(file)

print("Зчитаний список:")
print(loaded_list)
