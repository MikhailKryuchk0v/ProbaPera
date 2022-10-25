a = list(map(float,input().split()))
s=00
for i in range (len(a)):
    s+=a[i]
    av=s/len(a)
for i in  range(len(a)):
    if a[i]==0:
        a[i] = av
print(a[i], end="")
    

