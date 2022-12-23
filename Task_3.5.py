 #5. Задайте число. Составьте список чисел Фибоначчи, в том числе 
 # для отрицательных индексов.

n = (int (input ('Введите n - ')))
fib1 = 0
fib2 = 1

new_list = [fib1, fib2]

for i in range (1, n):
    fib1, fib2 = fib2, fib1 + fib2    
    new_list.append(fib2)
fib1 = 0
fib2 = 1   
for i in range (n):
    fib1, fib2 = fib2, fib1 - fib2
    new_list.insert(0, fib1)
print(*new_list)    


 
    

