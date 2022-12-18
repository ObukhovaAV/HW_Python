#5. Реализуйте алгоритм перемешивания списка.
#Без функции shuffle из модуля random.

n = int (input('Введите длину списка - '))
print (n)
if n < 0:
    n*= -1
my_list = list (range (n))
print (my_list)
from random import randrange
new_list = my_list

for i in range (n):
   j = randrange (n)
   t = new_list[i]
   new_list [i] = new_list[j]
   new_list[j] = t
print (new_list)
