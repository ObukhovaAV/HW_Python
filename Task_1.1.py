# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным. 

n = int (input ('Введите число '))
print (n)
if 0 < n <= 5:
    print ('Это рабочий день')
elif n == 6 or n == 7:
    print ('Это выходной день ')
else:
    print ('Это не день недели')