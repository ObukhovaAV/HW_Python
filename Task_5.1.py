# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". 
# В тексте используется разделитель пробел.
from random import sample

def made_text(count, word='abc'):
    my_list = []
    for i in range(count):
        letter = sample(word, k=3)
        temp = ("".join(letter))
        my_list.append(temp)
    return my_list

text =  (' '.join(map(str, made_text(int(input("Введите длину текста ")), 'абв'))))
print(text)
print()
new_text = text.replace('абв', '')
print(new_text)



    
    
