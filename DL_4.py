import math
while 1:
    print("Межі діапазону натуральних чисел та крок") 
    a1=int(input("a1="))
    a2=int(input("a2="))
    k=int(input("k="))
    if 0<a1<a2  and 0<k<a2:
        break
    else:
        print('Помилка введення')
for i in range(a1,a2+1,k):
    print(math.factorial(i))