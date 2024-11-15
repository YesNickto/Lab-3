import json

filename = 'input.json'


def task() -> float:
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
        return 0.0

    total_sum = 0
    for item in data:
        try:
            score = item['score']
            weight = item['weight']
            total_sum += score * weight
        except KeyError:
            print("В словаре отсутствует ключ 'score' или 'weight'")

    return round(total_sum, 3)


print(task())
