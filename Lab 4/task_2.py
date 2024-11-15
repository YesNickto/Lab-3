import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]

    with open(OUTPUT_FILENAME, "w") as f:
        json.dump(data, f, indent=4)


if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")