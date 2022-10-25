def test(i):
    k = i
    while (k):
        d = k % 10
        k //=10
        if (d and i % d):
            return False
    return True 
n = int(input())
for i in range(1, n+1):
    if (test(i) and i % 10 !=0):
        print(i)
        
