# 2. Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

def find_factors (number):
   d = 2  
   new_list = []
   if number < 1:
      number *= -1
   while d <= number:
      if number % d == 0:
        new_list.append(d)
        number //= d
      else:
        d += 1
   return new_list


print("Простые множители числа - ", find_factors(int(input('Введите целое число - '))))
