
import requests
import json

quotes = []

for i in range(5):
    try:
        response = requests.get(
            "https://dummyjson.com/quotes/random",
            timeout=15
        )

        response.raise_for_status()
        data = response.json()

        quote = {
            "text": data["quote"],
            "author": data["author"]
        }

        quotes.append(quote)

        print("Цитата:", quote["text"])
        print("Автор:", quote["author"])
        print()

    except Exception as error:
        print("Помилка:", error)

with open("quotes.json", "w", encoding="utf-8") as file:
    json.dump(quotes, file, ensure_ascii=False, indent=4)

print("Збереження завершено!")