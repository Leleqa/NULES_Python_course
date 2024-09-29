
import pandas as pd
from datetime import datetime

try:
    df = pd.read_csv('output.csv')
except Exception as e:
    print(f"Помилка відкриття csv файлу: {e}")
    exit()


def calculate_age(birth_date):
    birth_date = datetime.strptime(birth_date, '%d.%m.%Y')
    today = datetime.today()
    return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))


df['Вік'] = df['Дата народження'].apply(calculate_age)
df = df.drop(columns=['Стать', 'Посада', 'Місто проживання', 'Місто проживання', 'Адреса проживання',
                      'Адреса проживання', 'Адреса проживання', 'Телефон', 'Email'])

younger_18 = df[df['Вік'] < 18]
age_18_45 = df[(df['Вік'] >= 18) & (df['Вік'] <= 45)]
age_45_70 = df[(df['Вік'] > 45) & (df['Вік'] <= 70)]
older_70 = df[df['Вік'] > 70]

try:
    with pd.ExcelWriter('employees_by_age.xlsx', engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name='all', index=True)

        younger_18.to_excel(writer, sheet_name='younger_18', index=True)
        age_18_45.to_excel(writer, sheet_name='18-45', index=True)
        age_45_70.to_excel(writer, sheet_name='45-70', index=True)
        older_70.to_excel(writer, sheet_name='older_70', index=True)
except Exception as e:
    print(f"Помилка запису в xlsx файл: {e}")
    exit()

print("OK!")
