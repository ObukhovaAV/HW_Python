#5. Даны два файла, в каждом из которых находится запись многочленов. 
# Задача - сформировать файл, содержащий сумму многочленов.

import polynom1
import polynom2
print(polynom1.polynomial(int(input('Enter pow 1\n'))))
print(polynom2.polynomial(int(input('Enter pow 2\n'))))
data1 = open('poly1.txt', 'r')
data2 = open('poly2.txt', 'r')
line_count1 = 0
line_count2 = 0
for line in data1, data2:
    line_count1 += 1
    line_count2 += 1
if line_count1 == line_count2:
    for line1 in data1:
        line1 = line1.replace('= 0', '+')
    for line2 in data2:    
        with open ('poly.txt', 'a') as new_f:
            new_f.write(f'{line1.rstrip()} {line2}')
    
        
    




