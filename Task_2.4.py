#  4. Напишите программу, которая принимает на вход 2 числа.
# Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).
N = int (input ('Введите число - '))
print (N)
pos_one = int (input ('Введите номер первой позиции в списке -  '))
print (pos_one)
pos_two = int (input ('Введите номер второй позиции в списке -  '))
print (pos_two)
num_list = []
for i in range (-N, N+1):
    num_list.append (i)
print (num_list)
if 0 < pos_one <= len(num_list) and 0 < pos_two <= len(num_list):
    comp = num_list [(pos_one - 1)] * num_list [(pos_two - 1)]
    print ('Произведение элементов на указанных позициях = ', comp)
else:
    print ('Нет значений для этих позиций')