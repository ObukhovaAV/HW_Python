# 1. Вычислить число с заданной точностью d

from decimal import Decimal

def accurancy(number, d):
    number = Decimal(number)
    number = number.quantize(Decimal(d))
    return number

print (accurancy(input('Введите число - '), input('Введите заданную точность "0.0001" - ')))
