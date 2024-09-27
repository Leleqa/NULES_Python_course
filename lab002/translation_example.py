from googletrans import Translator
import pandas as pd

translator = Translator()


def LangDetect(txt):
    try:
        detectMap = {"Lang": translator.detect(
            txt).lang, "Confidence": str(translator.detect(txt).confidence)}
    except Exception as e:
        print(
            f"An error occured while trying to detect language using googletrans API: {e}")
        return None
    else:
        return detectMap


def TranSlate(txt, lang):
    try:
        translatedStr = str(translator.translate(txt, dest=lang).text)
    except Exception as e:
        print(
            f"An error occured while trying to translate a string using googletrans API: {e}")
        return None
    else:
        return translatedStr


def CodeLang(code):
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


print("Введіть текст для перекладу:")
txt = input()
print("Введіть мову, на яку перекладати:")
lang = input()

langDetectList = LangDetect(txt)

langName = CodeLang(langDetectList['Lang'])

print("Detected(lang=" + langDetectList['Lang'] +
      ", confidence=" + langDetectList['Confidence'] + ")")
print("ISO код " + langDetectList['Lang'] +
      " відповідає мові '" + langName + "'")
print(TranSlate(txt, lang))

print("Starting detect lang test:")
lang = input("Enter a language name or code: ")
print(f"The language name/code is '{CodeLang(lang)}'")
lang = input("Enter another language name or code: ")
print(f"The language name/code is '{CodeLang(lang)}'")
