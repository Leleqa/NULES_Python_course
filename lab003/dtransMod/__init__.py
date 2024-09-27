# __init__.py
from .my_dtrans_lib import LangDetect, TranSlate, CodeLang, LanguageList
import pandas as pd
from deep_translator import GoogleTranslator
# from langdetect import detect, DetectorFactory
from langdetect import detect_langs
from langdetect.lang_detect_exception import LangDetectException

NAME = "Text translation"
AUTHOR = "Volodmymyr Yalovenko, ki-21012b"


__all__ = ['LangDetect', 'TranSlate',
           'CodeLang', 'translate_table', 'translator']
