# -*- coding: utf-8 -*-
"""w3_ArolRakoto.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UmDf51fySHAh690fzjMPIq_e1LbXE58H
"""

# 1)
def number(input):
  total= sum(input)
  maximum= max(input)
  minimum = min(input)
  average = total/len(input)
  return(total, maximum, minimum, average)

numbers = [1,2,3,4,5]
number(numbers)

# 2)
def similarity(list1, list2):
  for element1 in list1:
    for element2 in list2:
      if element1 == element2:
        return "true"
  return "false"


first_1 = ['Tom', 'Bob', 'Sue', 'Rachel']
second_2= ['Bob', 'Susan', 'Roger', 'Mike']
similarity(first_1, second_2)

# 3)
def combine_dic(input1, input2):
  for key in input2:
    if key in input1:
     input2[key] += input1[key]

  new_dic = {**input1, **input2}

  return new_dic

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
combine_dic(d1,d2)

# 4)
for n in range(100):
  if (n%3==0):
    if (n%5==0):
      print("Fizzbuzz")
    else:
      print("Fizz")
  elif (n%5==0):
    print("Buzz")
  else:
    print(n)

# 5)
u, l, d, p = 0, 0,0,0
password = input()
if 16>=len(password)>=6:
  for i in password:
    if i.islower():
      l +=1
    if i.isupper():
      u +=1
    if i.isdigit():
      d +=1
    if (i=="$" or i=="#" or i=="@"):
      p +=1
if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(password)):
    print("Valid Password")
else:
    print("Invalid Password")

# 6)
new_list=[]
def unique_val(input):
  new_list = list(set(input))
  return(new_list)


a= [1,2,3,3,3,3,4,5]
unique_val(a)

# 7)
import math
def len_hypotenus(a,b):
  c = math.sqrt((a**2) + (b**2))
  return c

a = 12
b= 7
len_hypotenus(a,b)

# 8)
def scrable_score(letter):
  score = 0
  score_range = ("A,E,I,O,U,L,N,R,S,T", "D,G", "B,C,M,P", "F,H,V,W,Y", "K", "J,Y", "Q,Z")
  for letters in letter:
      letters = letters.upper()
      for indx in range(0, len(score_range),1):
        if letters in score_range[indx]:
          if indx ==0:
            score +=1
          elif indx==1:
            score +=2
          elif indx==2:
            score +=3
          elif indx==3:
            score +=4
          elif indx==4:
            score +=5
          elif indx==5:
            score +=8
          else:
            score +=10
  return score

name = "cabbage"
scrable_score(name)

# 9)
def great_common_divisor(a, b):
  for n in range(1, (min(a,b))):
    if a%n ==0 and b%n ==0:
      if n > 1:
        res = n
      else:
        res = 1
  return res

a = 27
b = 81
great_common_divisor(a, b)
