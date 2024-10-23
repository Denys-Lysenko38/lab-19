animals_ua_to_en = {
    'кіт': 'cat',
    'собака': 'dog',
    'лев': 'lion',
    'тигр': 'tiger',
    'слон': 'elephant',
    'ведмідь': 'bear',
    'зайць': 'hare',
    'лисиця': 'fox',
    'вовк': 'wolf',
    'білка': 'squirrel'
}

animals_en_to_ua = {en: ua for ua, en in animals_ua_to_en.items()}

print("Словник англійська -> українська:")
for key, value in animals_en_to_ua.items():
    print(f"{key} : {value}")