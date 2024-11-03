import psycopg2
import sys
import os
from faker import Faker
from psycopg2 import sql

# Параметри підключення до бази даних PostgreSQL
db_params = {
    'dbname': 'mydatabase',      # Назва бази даних
    'user': 'myuser',            # Ім'я користувача
    'password': 'mypassword',    # Пароль користувача
    'host': 'localhost',         # Адреса сервера
    'port': '5432'               # Порт
}
fake = Faker(locale='uk_UA')


# Створення з'єднання та курсора
try:
    conn = psycopg2.connect(**db_params)
    conn.autocommit = True  # автоматично фіксує транзакції
    cursor = conn.cursor()

    cursor.execute("""
        DROP TABLE IF EXISTS Оренда;
        DROP TABLE IF EXISTS Орендарі;
        DROP TABLE IF EXISTS Приміщення;
        """)

    # Створення таблиці Орендарі
    cursor.execute("""
        CREATE TABLE Орендарі (
    Код_орендаря SERIAL PRIMARY KEY,
    Назва_фірми VARCHAR(100) NOT NULL,
    Керівник VARCHAR(100),
    Телефон VARCHAR(30) CHECK (Телефон ~ '[0-9]')
        );
    """)
    print("Таблиця Орендарі створена.")

    # Створення таблиці Приміщення
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Приміщення (
            Номер_приміщення SERIAL PRIMARY KEY,
    Площа FLOAT NOT NULL,
    Вартість_оренди_за_м2 DECIMAL(10, 2) NOT NULL,
    Поверх INTEGER,
    Телефон_в_приміщенні BOOLEAN DEFAULT FALSE,
    Оздоблення VARCHAR(20) CHECK (Оздоблення IN ('звичайне', 'поліпшене', 'євро'))
        );
    """)
    print("Таблиця Приміщення створена.")

    # Створення таблиці Оренда
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Оренда (
            Номер_договору SERIAL PRIMARY KEY,
    Дата_початку DATE NOT NULL,
    Строк_дії_договору INTEGER CHECK (Строк_дії_договору > 0),
    Мета_оренди VARCHAR(50) CHECK (Мета_оренди IN ('офіс', 'кіоск', 'склад')),
    Код_орендаря INTEGER REFERENCES Орендарі(Код_орендаря)
        ON DELETE CASCADE ON UPDATE CASCADE,
    Номер_приміщення INTEGER REFERENCES Приміщення(Номер_приміщення)
        ON DELETE CASCADE ON UPDATE CASCADE
        );
    """)
    print("Таблиця Оренда створена.")

    ORENDAR_DATA = {"ID": [],
                    "NAME": [],
                    "OWNER": [],
                    "PHONE": []}
    for i in range(0, 5):
        ORENDAR_DATA["ID"].append(
            str(fake.unique.random_int(min=111111, max=999999)))
        ORENDAR_DATA["NAME"].append(fake.catch_phrase())
        ORENDAR_DATA["OWNER"].append(fake.name())
        ORENDAR_DATA["PHONE"].append(fake.msisdn())
    # breakpoint()
    for i in range(0, 5):
        cursor.execute("""
                        INSERT INTO Орендарі(Код_орендаря, Назва_фірми, Керівник, Телефон) VALUES(%s, %s, %s, %s)
                       """, (ORENDAR_DATA["ID"][i], ORENDAR_DATA["NAME"][i],
                       ORENDAR_DATA["OWNER"][i], ORENDAR_DATA["PHONE"][i]))

    cursor.execute("SELECT * FROM Орендарі")
    for record in cursor:
        print(record)

except Exception as e:
    print(f"Виникла помилка: {e}")
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno)
finally:
    cursor.close()
    conn.close()
