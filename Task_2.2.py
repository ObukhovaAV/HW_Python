#2. Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N в виде списка.

N = int (input ('Введите N - '))
print (N)
my_list = []
f = 1
for i in range (1, N+1):
    f = f * i
    my_list.append (f) 
print (my_list)  
