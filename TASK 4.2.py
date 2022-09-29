#VAR 9
n = int(input())
def nextFib(lastfib):
        buff = lastfib[1]
        lastfib[1] = lastfib[0] + lastfib[1]
        lastfib[0] = buff
        return lastfib
def fibSum(n):
        if n == 1:
                return 1
        if n == 2:
                return 3
        if n > 2:
                sum = 3
                lastfib = [1,2]
                for i in range(n-2):
                        lastfib = nextFib(lastfib)
                        sum+=lastfib[1]
                return sum

print(fibSum(n))