# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BsC_fxiOL91oMlU7HFc_Greg7q65b5EZ
"""

def assignment(a,b):
  if type(a) == type(b)== int:
    print(a+b)
    print(a-b)
    print(a*b)
    print(round(a/b*100,2),'%')
  elif type(a) == type(b)== str:
    print(a+b, '\nOther operations are not available')
  else:
    print(a*b)
    a = str(a)
    b = str(b)
    print(a+b)
