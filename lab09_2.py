import numpy as np

websites = {'example.com', 'test.org', 'python.org', 'github.com'}

websites_tuple = tuple(websites)
websites_list = list(websites)
websites_array = np.array(list(websites))

print("Множина (у рядок):", websites)
print("Множина (у стовпчик):")
for site in websites:
    print(site)

print("\nКортеж:", websites_tuple)
print("Список:", websites_list)
print("Масив NumPy:", websites_array)