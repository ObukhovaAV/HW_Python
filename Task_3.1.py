#1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
#Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётных позициях(не индексах).
from random import sample
def fill_list (count):
    some_list = sample (range (1, count*2), k=count)
    return (some_list)

def find_sum (some_list):
    sum = 0
    for i in range (len(some_list)):
      if i % 2 == 0: 
        sum = sum + (some_list[i])
    else:
        sum = sum + 0
    return sum


my_list = (fill_list (int (input('Введите длину списка - '))))
print (my_list)
print (find_sum (my_list))

 
    
    
