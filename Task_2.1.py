# 1. Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Без работы с методами строк.

number = float (input('Введите число - '))
print (number)

while number%10 != 0 : 
       number = number * 10
new_number = round(number)
print (new_number)
while new_number > 0: 
      sum = 0    
      sum = sum + new_number%10
      new_number = new_number / 10
print (sum)
