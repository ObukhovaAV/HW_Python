#2. Напишите программу, которая найдёт произведение пар чисел списка.
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.
from random import sample
def fill_list (count):
    some_list = sample (range (1, count * 3), k=count)
    return some_list

first_list = fill_list (int (input ('Введите длину списка - ')))
print (first_list)
comp_list = []
l = len(first_list)
for i in range ((l+1)// 2):
    if i == (l // 2):
        comp = first_list[i]
    else:
        comp = first_list[i] * first_list [l-1-i]        
    comp_list.append (comp)
 
print (comp_list)
