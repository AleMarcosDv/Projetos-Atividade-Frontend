# -*- coding: utf-8 -*-
"""Atvdd_idade.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1O-LTHZ8Lh-DesXOXgy8krM4eNL4y7Ael
"""

nm = str(input("Insira seu nome: "))

exe = True

while(exe == True):
  try:
    num = int(input("Insira seu ano de nascimento: "))
    if (num < 1922) or (num > 2021):
      print("Use um ano antes de 2021 e após 1922")
    elif(num >= 1922 or num <= 2021):
      idd = 2021 - num
      idd2 = idd + 1
      print(F"O Sr.(a) {nm} tem {idd} anos, e ira fazer {idd2} anos ano que vem.")
      exe = False
  except:
    print("Use apenas números onde solicitado.")