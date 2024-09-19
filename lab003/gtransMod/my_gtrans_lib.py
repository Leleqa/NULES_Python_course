import pandas as pd
from googletrans import LANGUAGES, Translator

translator = Translator()


def LangDetect(txt: str, seto: str):
    temp = []
    try:
        if seto == "lang":
            temp = translator.detect(txt).lang
        elif seto == "confidence":
            temp = str(translator.detect(txt).confidence)
        elif seto == "all":
            temp = [translator.detect(txt).lang, str(
                translator.detect(txt).confidence)]
        else:
            return None

    except Exception as e:
        print(
            f"An error occured while trying to detect language using googletrans API: {e}")
        return None
    else:
        return temp


def TranSlate(txt: str, dlang: str, slang: str = "auto"):
    try:
        if slang == "auto":
            translatedStr = str(translator.translate(
                txt, dest=dlang, src=slang).text)
        else:
            translatedStr = str(translator.translate(
                txt, dest=dlang).text)
    except Exception as e:
        print(
            f"An error occured while trying to translate a string using googletrans API: {e}")
        return None
    else:
        return translatedStr


def CodeLang(code: str):
    if len(code) < 3:
        try:
            df = pd.read_csv("iso_639-1.csv")
            lang = df.loc[df["639-1"] == code, "name"].values[0]
        except Exception as e:
            print(f"Failed to find code {code}: {e}")
            return None
        else:
            return lang

    else:
        try:
            df = pd.read_csv("iso_639-1.csv")
            iso = df.loc[df["name"] == code, "639-1"].values[0]
        except:
            print(f"Failed to find language {code}")
            return None
        else:
            return iso


def translateTable(text=None, out="screen"):
    translator = Translator()
    # Створюємо заголовок таблиці
    if text:
        table_header = f"{'Language':<30}{'Code':<10}{'Translated Text':<50}"
    else:
        table_header = f"{'Language':<30}{'Code':<10}"
    # Записуємо рядки для кожної мови
    table_rows = []
    for code, language in LANGUAGES.items():
        if text:
            try:
                translated = translator.translate(text, dest=code).text
            except Exception as e:
                return f"Error translating to {language}: {e}"
            row = f"{language:<30}{code:<10}{translated:<50}"
        else:
            row = f"{language:<30}{code:<10}"
        table_rows.append(row)
    # Формуємо таблицю
    table = "\n".join([table_header] + table_rows)

    # Виводимо на екран або в файл
    if out == "screen":
        print(table)
        return 'Ok'
    elif out == "file":
        try:
            with open('languages_table.txt', 'w', encoding='utf-8') as file:
                file.write(table)
            return 'Ok'
        except Exception as e:
            return f"Error writing to file: {e}"
    else:
        return "Invalid output option. Use 'screen' or 'file'."
