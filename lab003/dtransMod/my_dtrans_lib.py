import pandas as pd
from deep_translator import GoogleTranslator
# from langdetect import detect, DetectorFactory
from langdetect import detect_langs
from langdetect.lang_detect_exception import LangDetectException

# DetectorFactory.seed = 0  # Для стабільності результатів detect()


def LangDetect(txt: str, seto: str):
    temp = []
    try:
        if seto == "lang":
            temp = detect_langs(txt)
            temp = [str(element) for element in temp]
            temp = temp[0][:2]
        elif seto == "confidence":
            temp = detect_langs(txt)
            temp = [str(element) for element in temp]
            temp = temp[0][3:8]
        elif seto == "all":
            temp1 = detect_langs(txt)
            temp1 = [str(element) for element in temp]
            temp1 = temp[0][:2]

            temp2 = detect_langs(txt)
            temp2 = [str(element) for element in temp]
            temp2 = temp[0][3:8]

            temp = [temp1, temp2]
        else:
            return None

    except LangDetectException as e:
        print(
            f"An error occurred while trying to detect language using langdetect: {e}")
        return None
    else:
        print(temp)
        return temp


def TranSlate(txt: str, dlang: str, slang: str = ""):
    try:
        if slang == "":
            detected = detect_langs(txt)
            detected = [str(element) for element in detected]
            """
            print("\n\n")
            print(detected)
            """
            translatedStr = GoogleTranslator(
                source=detected[0][:2], target=dlang).translate(txt)
        else:
            print("Entered not auto")
            translatedStr = GoogleTranslator(
                source=slang, target=dlang).translate(txt)
    except Exception as e:
        print(
            f"An error occurred while trying to translate a string using deep-translator API: {e}")
        return None
    else:
        return translatedStr


def CodeLang(code: str):
    if len(code) < 3:
        try:
            df = pd.read_csv("iso_639-1.csv")
            lang = df.loc[df["639-1"] == code, "name"].values[0]
        except:
            print(f"Failed to find code {code}")
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
    translator = GoogleTranslator(source='auto', target='en')
    supported_languages = translator.get_supported_languages(as_dict=True)

    if text:
        table_header = f"{'Code':<30}{'Language':<10}{'Translated Text':<50}"
    else:
        table_header = f"{'Language':<30}{'Code':<10}"

    table_rows = []
    for code, language in supported_languages.items():
        if text:
            try:
                translated = GoogleTranslator(
                    source='auto', target=code).translate(text)
            except Exception as e:
                return f"Error translating to {language}: {e}"
            row = f"{language:<30}{code:<10}{translated:<50}"
        else:
            row = f"{language:<30}{code:<10}"
        table_rows.append(row)

    table = "\n".join([table_header] + table_rows)

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
