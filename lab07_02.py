import random

def process_multiple_strings(lines):
    for line in lines:
        if len(line) % 3 == 0:
            part_length = len(line) // 3
            parts = [line[i:i + part_length] for i in range(0, len(line), part_length)]
            random.shuffle(parts)
            print(''.join(parts))
        else:
            print("Довжина рядка не кратна 3.")

n = int(input("Введіть кількість рядків: "))

lines = [input(f"Введіть рядок {i+1}: ") for i in range(n)]

process_multiple_strings(lines)