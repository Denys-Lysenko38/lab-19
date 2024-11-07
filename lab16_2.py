import matplotlib.pyplot as plt

areas = {}
with open('areas.txt', 'r', encoding='utf-8') as file:
    for line in file:
        try:
            region, area = line.strip().split(' : ')
            areas[region] = int(area)
        except ValueError:
            print(f"Невірний формат рядка: {line.strip()}")

if areas:
    regions = list(areas.keys())
    area_values = list(areas.values())

    plt.barh(regions, area_values, color='skyblue')
    plt.xlabel('Площа (км²)')
    plt.ylabel('Області')
    plt.title('Площа областей України')
    plt.grid(axis='x')

    plt.show()
else:
    print("Не вдалося завантажити дані для побудови гістограми.")