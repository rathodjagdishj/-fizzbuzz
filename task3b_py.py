# -*- coding: utf-8 -*-
"""task3b.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14YAZRVGI0SbnFXYlPOl9f8Xq4XFItYQF
"""

import numpy as np # imported the numpy lib
import pandas as pd # import from pand

def count_the_article(book1): # function created
  book1 = open(book1,'r')
  lines = book1.readlines()
  words = ["a", "the", "at", "run", "to","and","are","or","for","an","this"] # as per given in question
  pd.value_counts(np.lines.array(words))