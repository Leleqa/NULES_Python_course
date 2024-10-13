#!python
import re
import sys

ukrainian_order = {char: idx for idx, char in enumerate(
    'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя')}


def custom_sort(lst):
    def sort_key(word):
        lower_word = word.lower()
        transformed = []
        for char in lower_word:
            if char in ukrainian_order:
                transformed.append(ukrainian_order[char])
            else:
                transformed.append(1000 + ord(char))
        return transformed
    return sorted(lst, key=sort_key)


try:
    filename = sys.argv[1]
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()

    first_sentence = re.split(r'[.!?]', text)[0].strip()
    print(f"Перше речення: {first_sentence}")

    words = re.findall(r'\b\w+\b', text)

    sorted_words = custom_sort(words)

    word_count = len(words)

    print(f"Відсортовані слова: {', '.join(sorted_words)}")
    print(f"Кількість слів: {word_count}")

except FileNotFoundError:
    print("Помилка: файл не знайдено.")
except IOError:
    print("Помилка: не вдалося прочитати файл.")
