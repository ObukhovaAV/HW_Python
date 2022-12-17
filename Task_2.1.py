# 1. Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Без работы с методами строк.

number = float (input('Введите число - '))
while number % 10 != 0 : 
       number = number * 10
new_number = int (number)
sum = 0
while new_number > 0: 
      sum = sum + int (new_number) % 10
      new_number = int (new_number) / 10
print ('Сумма цифр числа = ', sum)
