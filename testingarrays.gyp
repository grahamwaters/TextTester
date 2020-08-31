import re
import string
import time
import numpy as nmp
import nltk
import pandas
#nltk.download()
#import matplotlib.pyplot as plt
#import pandas as pd
from nltk.corpus import wordnet as wn
from datetime import datetime
from tqdm import tqdm
from tqdm import tqdm_gui
import pdfminer
from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

textMATCH = '''now,[1319]
eyes,[1484, 1549]
voice,[1575, 1628, 1829]
me,[1682]
sorrow,[1794, 1799, 1859]
offering,[2106, 2141]
deep,[1272]
divided,[59, 113]
first,[84, 1029] '''


#array creation
multarrays = []
arr1 = []
arr2 = []
text_string = textMATCH
#text_string = textMATCH.read().lower()
fulltext = text_string
alltext = re.findall(r'\b[a-z]{2,15}\b', fulltext)
actword = ""
for word in tqdm(fulltext):
    if word == '\n':
        multarrays.append(actword)
        actword = ""
    elif word != " ":
        actword = actword + word
    elif word == ' ':
        multarrays.append(actword)
        actword = ""  
    else:
        arr1.append(word)#  TESTING DYNAMIC ARRAY 7/30/20


print(multarrays)