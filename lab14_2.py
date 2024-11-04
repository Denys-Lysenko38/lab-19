import requests
from bs4 import BeautifulSoup

def save_links_text(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        links_text = [link.get_text(strip=True) for link in soup.find_all('a') if link.get_text(strip=True)]

        with open('links_text.txt', 'w') as file:
            for text in links_text:
                file.write(text + '\n')
        
        print(f"Текст гіперпосилань збережено в файл 'links_text.txt'")
    except requests.RequestException as e:
        print("Помилка запиту:", e)

url = input("Введіть URL-адресу веб-сторінки: ")
save_links_text(url)