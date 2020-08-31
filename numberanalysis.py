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


i = 0 
top = 10000
match = 0
while y<top:

    while i<top:
        
        if i > 10 and i < 100:
            if dig1 % y == 0:
            match = match + 1
        if dig2 % y == 0:
            match = match + 1
        if dig3 % y == 0:
            match = match + 1
        
       

        i+=1

    y+=1
'''
if dig1 % y == 0:
            match = match + 1
        if dig2 % y == 0:
            match = match + 1
        if dig3 % y == 0:
            match = match + 1
        if dig4 % y == 0:
            match = match + 1
        if dig5 % y == 0:
            match = match + 1'''