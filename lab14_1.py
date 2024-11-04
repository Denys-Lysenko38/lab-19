import requests
from bs4 import BeautifulSoup
import json

def count_tags(url, tag):
    try:
        # Надсилаємо запит на вказаний URL
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Підраховуємо кількість тегів
        tags_count = len(soup.find_all(tag))
        
        # Зберігаємо результат у JSON
        result = {
            'url': url,
            'tag': tag,
            'count': tags_count
        }
        with open('tag_count.json', 'w') as json_file:
            json.dump(result, json_file, indent=4)
        
        print(f"Кількість тегів <{tag}> на сторінці: {tags_count}")
    except requests.RequestException as e:
        print("Помилка запиту:", e)

# Введення користувачем URL-адреси та HTML-тега
url = input("Введіть URL-адресу веб-сторінки: ")
tag = input("Введіть HTML-тег для підрахунку: ")
count_tags(url, tag)