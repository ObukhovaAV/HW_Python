# 1. Вычислить число с заданной точностью d

from decimal import Decimal

number = Decimal(input('Введите число - '))
d = input ('Введите зададанную точность "0.0001" - ')
number = number.quantize(Decimal(d))
print(number)       
