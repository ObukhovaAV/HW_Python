#1. Представлен список чисел. Необходимо вывести элементы исходного списка, 
# значения которых больше предыдущего элемента. Use comprehension.

from random import sample
def fill_list(n):
    ls = sample (range(n*3), k=n)    
    return ls

def sort_list(some_list):
    ls = [some_list[i] for i in range(1, len(some_list)) if some_list[i] > some_list[i - 1]]
    return ls

my_l = list(fill_list(int(input('Введите длину списка n '))))
print(my_l)
new_l = print(sort_list(my_l))




