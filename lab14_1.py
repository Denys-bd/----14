import requests
from bs4 import BeautifulSoup
import json

url = input("Введіть адресу веб-сторінки: ")

keywords = input("Введіть ключові слова через пробіл: ").lower().split()

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    text = soup.get_text().lower()

    results = {}

    for word in keywords:
        results[word] = text.count(word)

    print("Результати пошуку:")
    for word, count in results.items():
        print(word, "-", count)

    with open("keywords.json", "w", encoding="utf-8") as file:
        json.dump(results, file, ensure_ascii=False, indent=4)

    print("Результати збережено у файл keywords.json")

else:
    print("Помилка завантаження сторінки:", response.status_code)