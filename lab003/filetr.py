import configparser
import re
import os
from gtransMod import LangDetect, TranSlate, CodeLang


def text_statistics(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        # Count characters (including spaces)
        char_count = len(text)

        # Count words (split by whitespace)
        word_count = len(text.split())

        # Count sentences (ends with '.', '!', or '?')
        sentence_count = len(re.findall(r'[.!?]', text))

        return char_count, word_count, sentence_count
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None


def process_file(config):
    char_count = 0
    word_count = 0
    sentence_count = 0
    tempStr = []

    try:
        with open(config["Name"], 'r', encoding='utf-8') as file:
            for line in file:
                char_count += len(line)
                word_count += len(line.split())
                sentence_count += len(re.findall(r'[.!?]', line))

                tempStr += line

                # Перевірка на перевищення лімітів
                if char_count > int(config['stopAtXSymbol']):
                    print("Досягнута максимальна кількість символів.")
                    break
                if word_count > int(config['stopAtXWord']):
                    print("Досягнута максимальна кількість рядків.")
                    break
                if sentence_count > int(config['stopAtXSentance']):
                    print("Досягнута максимальна кількість речень.")
                    break

    except Exception as e:
        print(f"Failed during file processing: {e}")
        return None
    else:
        tempStr = ''.join(tempStr).strip()
        return str(tempStr)


try:
    config = configparser.ConfigParser()

except Exception as e:
    print(e)

try:
    config.read('config.ini')
except Exception as e:
    print(f"Failed to open the file: {e}")

if config.sections() != ['Options']:
    print("Failed to open config.ini: File does not exist or is corrupted")
    exit()

configDict = {
    "Name": config['Options']['fileName'],
    "Dest": config['Options']['destLang'],
    "outMethod": config['Options']['outMethod'],
    "stopAtXSymbol": config['Options']['stopAtXSymbol'],
    "stopAtXWord": config['Options']['stopAtXWord'],
    "stopAtXSentance": config['Options']['stopAtXSentance']
}
"""
fileName = config['Options']['fileName']
destLang = config['Options']['destLang']
outMethod = config['Options']['outMethod']
stopAtXSymbol = config['Options']['stopAtXSymbol']
stopAtXWord = config['Options']['stopAtXWord']
stopAtXSentance = config['Options']['stopAtXSentance']
"""

"""
print(configDict["Name"])
print(configDict['Dest'])
print(configDict['outMethod'])
print(configDict['stopAtXSymbol'])
print(configDict['stopAtXWord'])
print(configDict['stopAtXSentance'])
"""

char_count, word_count, sentence_count = text_statistics(configDict["Name"])

print(f"Назва файлу: {configDict["Name"]}")
print(f"Розмір файлу: {os.path.getsize(configDict['Name'])} біт")
print(f"Кількість символів: {char_count}")
print(f"Кількість слів: {word_count}")
print(f"Кількість речень: {sentence_count}")

txt = process_file(configDict)
print(txt)
print("LangDetectNext")
# pdb.set_trace()  # this will let you poke around... try "p x"
langDetectName = LangDetect(txt, "lang")
langDetectConf = LangDetect(txt, "confidence")

langName = CodeLang(langDetectName)

if configDict['outMethod'] == 'File':
    try:
        with open("output.txt", "w") as file:
            file.write("Detected(lang=" + langDetectName +
                       ", confidence=" + langDetectConf + ")" + "\nISO код " + langDetectName +
                       " відповідає мові '" + langName + "'\n\n" + TranSlate(txt, configDict["Dest"]))
    except Exception as e:
        print(f"Failed creating the output file: {e}")
    else:
        print("Ok")

else:
    print("\n\nDetected(lang=" + langDetectName +
          ", confidence=" + langDetectConf + ")")
    print("ISO код " + langDetectName +
          " відповідає мові '" + langName + "'\n\n")
    print(TranSlate(txt, configDict["Dest"]))
