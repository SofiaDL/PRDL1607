n1=int(input("Введіть початкове число"))
n2=int(input("Введіть кінцеве число"))
sp = [ ]
f1=0
f2=1
for i in range(n2+1):
    sp.append(f1)
    f1,f2 = f2,f2+f1
    if sp[i]>=n1 and sp[i]<=n2:
        print(sp[i],sep='')    
