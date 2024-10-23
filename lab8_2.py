from array import array

n = int(input("Введіть розмір масиву (n): "))

masiv = [array('i', [0]*n) for _ in range(n)]

num = 1
for col in range(n-1, -1, -1):
    for row in range(n):
        masiv[row][col] = num
        num += 1

print("Заповнений масив:")
for row in masiv:
    print(list(row))