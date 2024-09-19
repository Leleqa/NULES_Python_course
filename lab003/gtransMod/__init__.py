# __init__.py
from .my_gtrans_lib import LangDetect, TranSlate, CodeLang, translateTable
from googletrans import LANGUAGES, Translator
import pandas as pd
NAME = "Text translation"
AUTHOR = "Volodmymyr Yalovenko, ki-21012b"


translator = Translator()

__all__ = ['LangDetect', 'TranSlate',
           'CodeLang', 'translate_table', 'translator']
