from math import *
a = float(input("Введите число (в градусах): "))

while a % 180 == 135:
    print('Вы не можете ввести данное число! Попробуйте еще.')
    a = float(input("Введите число (в градусах): "))

z1 = int((1 - 2*pow(int(sin(radians(a))), 2))/(1 + int(sin(2*radians(a)))))
z2 = int((1 - tan(radians(a)))/(1 + tan(radians(a)))) 

if  a % 180 == 90:
    print("Значение Z1 = ",z1)
    print("Мы не можем вывести значение Z2, т.к. при таком значении tg = неопределн")
else:
    print("Значение Z1 = ",z1)
    print("Значение Z2 = ",z2)
