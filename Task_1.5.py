# Напишите программу, которая принимает на вход координаты двух точек и находит
# расстояние между ними в 2D пространстве
xA = int (input ('Введите координату x для точки A - '))
print (xA)
yA = int (input ('Введите координату y для точки A - '))
print (yA)
xB = int (input ('Введите координату x для точки B - '))
print (xB)
yB = int (input ('Введите координату y для точки B - '))
print (yB)
distance = ((xB-xA)**2 + (yB-yA)**2)**0.5
print (round (distance, 3))
