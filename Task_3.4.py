#4. Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
#Напишите программу, которая найдёт разницу между максимальным и минимальным значением
#  дробной части элементов.

from random import uniform
n = int (input('Введите длину списка - '))
my_list = []
for i in range (n):
    elem = uniform (0, 10)
    my_list.append (round (elem, 2))
print (my_list)

for i in range (len(my_list)):
    my_list[i] = int (my_list[i]*100)
    my_list[i] = (my_list[i])%100

max = min = my_list[0]
for i in range (len(my_list)):    
    if my_list[i] > max:
       max = my_list[i]

for i in range (len(my_list)):    
    if my_list[i] < min:
        min = my_list[i]   
a, b = max, min     
diff = a - b
print ('Разница между максимальным и минимальным значением  дробной части = ', diff)

    