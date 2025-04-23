import json
from datetime import datetime

RESULTS_FILE = "game_results.json"

def save_result(name, rounds, score):
    result = {
        "Дата": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Игрок": name,
        "Количество раундов": rounds,
        "Итоговый счет": f"{score:+d}"
    }

    try:
        with open(RESULTS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    data.append(result)

    with open(RESULTS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def get_results():
    try:
        with open(RESULTS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            for entry in data:
                print(f"Дата: {entry['Дата']}")
                print(f"Игрок: {entry['Игрок']}")
                print(f"Количество раундов: {entry['Количество раундов']}")
                print(f"Итоговый счет: {entry['Итоговый счет']}")
                print("-" * 40)
    except FileNotFoundError:
        print("Результатов пока нет.")