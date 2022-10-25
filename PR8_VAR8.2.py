arr=[]
for i in range(int(input().strip())):
    arr.append(input().strip().split(" "))
print(*[' '.join(i) for i in zip(*arr)],sep='\n')  