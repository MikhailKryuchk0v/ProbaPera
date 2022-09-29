#VAR 10
n = int(input())
k = int(input())


def nextFib(lastfib):
    buff = lastfib[1]
    lastfib[1] = lastfib[0] + lastfib[1]
    lastfib[0] = buff
    return lastfib


def fibSum(n, k):
    sum = 3
    lastfib = [1, 2]
    if n > k:
        buff = n
        n = k
        k = buff
    for i in range(n - 3):
        sum += lastfib[1]
    for i in range(k - 2):
        lastfib = nextFib(lastfib)
        sum += lastfib[1]

    if n == 1:
        return sum
    if n == 2:
        return sum - 1
    if n >= 3:
        return sum - 3


print(fibSum(n, k))