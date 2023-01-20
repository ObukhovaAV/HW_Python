# 2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.

def fill_list(n):
    ls1 = [i for i in range(20, n + 1) if not i % 20 or not i % 21]
    return ls1

N = int(input("Введите N "))
print(fill_list(N))