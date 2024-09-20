from gtransMod import LangDetect, TranSlate, CodeLang, LanguageList


print("Введіть текст для перекладу:")
txt = input()
print("Введіть мову, на яку перекладати:")
dlang = input()
print("Введіть мову, з якої перекладати (або нічого для автоматичного визначення):")
slang = input()

langDetectName = LangDetect(txt, "lang")
langDetectConf = LangDetect(txt, "confidence")

langName = CodeLang(langDetectName)

print("Detected(lang=" + langDetectName +
      ", confidence=" + langDetectConf + ")")
print("ISO код " + langDetectName +
      " відповідає мові '" + langName + "'")
print(TranSlate(txt, dlang, slang))

print("Starting detect lang test:")
lang = input("Enter a language name or code: ")
print(f"The language name/code is '{CodeLang(lang)}'")
lang = input("Enter another language name or code: ")
print(f"The language name/code is '{CodeLang(lang)}'")

result = LanguageList("Hello, world!", out="screen")
print(result)
