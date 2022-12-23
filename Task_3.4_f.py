#4. Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
#Напишите программу, которая найдёт разницу между максимальным и минимальным значением
#  дробной части элементов.

from random import uniform

def fill_list (n):
    new_list = []
    for i in range (n):
        elem = uniform (0, 10)
        new_list.append (round (elem, 2))
    return (new_list)

def trans_list (some_list):
    for i in range (len(some_list)):
        some_list[i] = int (some_list[i]*100)
        some_list[i] = (some_list[i])%100
    return some_list

def find_min_and_max (some_list):
    max = min = some_list[0]
    for i in range (len(some_list)):    
        if some_list[i] > max:
           max = my_list[i]
    
    for i in range (len(some_list)):    
        if some_list[i] < min:
           min = some_list[i]  
    return min, max 
    

my_list = fill_list(int(input('Введите длину списка - ')))
print (my_list)
new_list = trans_list(my_list)
a, b = find_min_and_max(new_list)
print ('Разница между максимальным и минимальным значением  дробной части = ', b - a)