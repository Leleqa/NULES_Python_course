import pandas as pd
from faker import Faker
from random import randint


def init_csv_data():
    temp = {
        'Прізвище': [],
        "Ім'я": [],
        'По батькові': [],
        'Стать': [],
        'Дата народження': [],
        'Посада': [],
        'Місто проживання': [],
        'Адреса проживання': [],
        'Телефон': [],
        'Email': []
    }
    return temp


def get_sex():
    num = randint(1, 10)
    if num < 5:
        return 'Жінка'
    else:
        return 'Чоловік'


# def get_father():


def fill_csv(data: dict, numRecords: int = 2000):
    for _ in range(numRecords):
        sex = get_sex()
        if sex == 'Жінка':
            data['Прізвище'].append(fake.last_name_female())
            data["Ім'я"].append(fake.first_name_female())
            data['По батькові'].append(fake.middle_name_female())
        else:
            data['Прізвище'].append(fake.last_name_male())
            data["Ім'я"].append(fake.first_name_male())
            data['По батькові'].append(fake.middle_name_male())

        data['Стать'].append(sex)
        data['Дата народження'].append(
            fake.date_of_birth(minimum_age=16, maximum_age=85).strftime('%d.%m.%Y'))
        data['Посада'].append(fake.job())
        data['Місто проживання'].append(fake.city())
        data['Адреса проживання'].append(fake.address().replace("\n", ", "))
        data['Телефон'].append(fake.phone_number())
        data['Email'].append(fake.email())
    return data


fake = Faker(locale='uk_UA')

data = init_csv_data()
fill_csv(data)
df = pd.DataFrame(data)

df.to_csv('output.csv', index=False)

print("CSV file created!")
