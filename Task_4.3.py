# 3. Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов
#  исходной последовательности в том же порядке.

from random import choices

def fill_list(count):
   if count<=0:
    return ('Negative value of the number of numbers!')
   else:
    some_list = choices (range (1, count), k=count)
   return some_list
   
def list_sort(some_list):
   new_list=[]
   for i in range (len(some_list)):    
       if some_list.count(some_list[i]) == 1:
           new_list.append(some_list[i])
   return (new_list)   
      
list_1 = fill_list(int(input('Введите длину списка - ')))
print(list_1)    
list_2 = list_sort(list_1)
print(list_2)



   
