import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import pdb


def calculate_age(birth_date):
    birth_date = datetime.strptime(birth_date, '%d.%m.%Y')
    today = datetime.today()
    return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))


def read_csv_file(filename):
    try:
        df = pd.read_csv(filename)
        print("Файл відкрито успішно: Ok")
        return df
    except Exception as e:
        print(f"Помилка при обробці файлу: {e}")
        return None


def analyze_data(df):
    df['Вік'] = df['Дата народження'].apply(calculate_age)

    sex_size = df['Стать'].value_counts("Жінка")
    print(sex_size)
    # breakpoint()

    plt.figure(figsize=(6, 6))
    plt.pie(sex_size, labels=['Чоловіки', 'Жінки'],
            autopct='%1.1f%%', startangle=15, colors=['skyblue', 'Pink'])

    plt.title('Кількість співробітників за статтю')
    plt.ylabel('')
    plt.show()

    categories = {
        'younger_18': (df['Вік'] < 18),
        '18_45': (df['Вік'] >= 18) & (df['Вік'] <= 45),
        '45_70': (df['Вік'] > 45) & (df['Вік'] <= 70),
        'older_70': (df['Вік'] > 70)
    }

    category_counts = {category: df[mask].shape[0]
                       for category, mask in categories.items()}
    print("\nКількість співробітників за віковими категоріями:")
    for category, count in category_counts.items():
        print(f"{category}: {count}")

    plt.figure(figsize=(6, 6))
    plt.bar(category_counts.keys(), category_counts.values(),
            color=['Red', 'Green', 'Yellow', 'Blue'])
    plt.title('Кількість співробітників за віковими категоріями')
    plt.xlabel('Вікові категорії')
    plt.ylabel('Кількість')
    plt.show()

    print("\nКількість співробітників за статтю в кожній віковій категорії:")
    for category, mask in categories.items():
        sex_by_category = df[mask]['Стать'].value_counts('Жінка')
        print(f"\nКатегорія {category}:")

        plt.figure(figsize=(6, 6))
        plt.pie(sex_by_category, labels=['Чоловіки', 'Жінки'],
                autopct='%1.1f%%', startangle=15, colors=['skyblue', 'Pink'])
        plt.title(f'Кількість співробітників за статтю в категорії {category}')
        plt.ylabel('')
        plt.show()


filename = 'output.csv'
df = read_csv_file(filename)

if df is not None:
    analyze_data(df)
