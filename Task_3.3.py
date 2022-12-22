#3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#Без использования встроенной функции преобразования, без строк.

number = int (input ('Введите число - '))
my_list = []
while number:
    number_2 = number % 2
    number = number // 2
    my_list.append (number_2)
my_list.reverse ()
print ('Число в двоичном исчислении = ', "".join(map(str, my_list))) 
