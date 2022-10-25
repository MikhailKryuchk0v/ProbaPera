from random import random as r
n,k=map(int,input('n k > ').split())
k-=1; b=range(n)
a=[[r() for j in b] for i in b]; print(a)
for j in b: a[k][j]/=a[k][k]
print(a)