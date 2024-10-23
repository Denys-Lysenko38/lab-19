from array import array

masiv = array('i', [int(input(f"Введіть число {i+1}: ")) for i in range(10)])

average = sum(masiv) / len(masiv)
print(f"Середнє арифметичне: {average}")

new_masiv = array('i', [x for x in masiv if x <= average])

print("Масив після видалення чисел більших за середнє арифметичне:")
print(new_masiv)