# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n 
# и выведите на экран их сумму.

n = int (input('Введите n - '))
print (n)
new_list = []
sum = 0
for i in range (1, n+1):
    i = round ((1 + 1/i) ** i, 3)
    new_list.append (i) 
    sum = sum + i  
print (new_list)
print (sum)


