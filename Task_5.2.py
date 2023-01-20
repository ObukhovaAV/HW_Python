# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def rle_encode(my_str = 'text_words.txt', code_text='text_code_words.txt'):
    string = open(my_str, 'r')
    line_string = string.readlines()
    with open(code_text, 'a') as my_f:
        for i in line_string:
            count = 1
            for j in range(len(i.strip()) - 1):
                if i[j] == i[j + 1]:
                    count += 1
                else:
                    my_f.write(f'{count}{i[j]}')
                    count = 1 
            my_f.write(f'{count}{i[j + 1]}')             
            my_f.write('\n')

def rle_decode(s_str = 'text_code_words.txt'): 
    string = open(s_str, 'r')
    line_string = string.readlines()
    for i in line_string:
        n = ''
        symbols = []      
        for j in i.strip():
            if j.isdigit():
                n += j
            else:
                symbols.append(int(n) * j)
                n = ''
        print(''.join(map(str, symbols)))

rle_encode(input("Enter the name of the file with the text: "), input("Enter the file name to record:"))
rle_decode(input("Enter the file name to decode:"))





