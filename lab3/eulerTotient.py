from math import gcd

m=int(input("Enter value of m: "))
list=[]

for i in range(0,m):
    list.append(i)

phi=0
for i in list:
    if gcd(i,m)==1:
        phi = phi+1

print(phi)
