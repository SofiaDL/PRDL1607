from  random import *
n=randint(1,100)
vn=int(input("Вгадай,яке число задумане від 1 до 100?"))
while (vn <0) or (vn > 100):
    vn=int(input("Введене число не  належить діапазону від 0 до 100,введіть ще раз число"))
while vn!=n:
    if vn<n:
        print("Введене число менше ніж задумане")
    else:
        print("Введене число більше ніж задумане")   
    vn=int(input("Спробуйте ще "))    
print("Ви виграли!!!")    