# -*- coding: utf-8 -*-
"""Cdg_atvd_calc.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jOw3Ic9rbLVyL70L0q1DpmRWLGpLQxHm
"""

print("Para calcular leve em consideração as operações são: 1 = Soma, 2 = Subtração, 3 = Multiplicação e 4 = Divisão")
print("Além de que deve se seguir uma sequência: numero1, numero2 e operação")




def calc(num1, num2, operador):
    if (operador == 0 or operador > 4):
      print("Numero de operação inválido")
      resp = 0
    elif (operador == 1):
      resp = num1 + num2
    elif (operador == 2):
      resp = num1 - num2
    elif (operador == 3):
      resp = num1 * num2
    elif (operador == 4):
          resp = num1 / num2
    return resp


num1 = int(input("Numero1?"))
num2 = int(input("Numero2?"))
operador = int(input("Número do operador?"))


resp = calc(num1, num2, operador)
print (resp)