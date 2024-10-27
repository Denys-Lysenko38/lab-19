import os

# Шлях до каталогу
directory = "QUESTIONS"

# Лічильник для .png файлів
png_count = 0
jpg_files = []
tiff_files = []

# Перебір файлів у каталозі
for filename in os.listdir(directory):
    if filename.endswith(".png"):
        png_count += 1
    elif filename.endswith(".jpg") or filename.endswith(".jpeg"):
        jpg_files.append(filename)
    elif filename.endswith(".tiff"):
        tiff_files.append(filename)

# Виведення кількості .png файлів
print("Кількість .png файлів:", png_count)

# Виведення списку .jpg(.jpeg) файлів
print("Список .jpg(.jpeg) файлів:")
for file in jpg_files:
    print(file)

# Запис імен .tiff файлів у tiff.txt
with open("tiff.txt", "w") as tiff_file:
    for file in tiff_files:
        tiff_file.write(file + "\n")
