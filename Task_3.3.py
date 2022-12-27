#3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#Без использования встроенной функции преобразования, без строк.

def num_trans (number):
    my_list = []
    while number:
        number_2 = number % 2
        number = number // 2
        my_list.append (number_2)
    my_list.reverse ()
    return my_list

my_list = num_trans(int(input('Введите число - ')))
print ('Число в двоичном исчислении = ', "".join(map(str, my_list))) 
