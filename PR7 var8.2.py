def func1 (a):
    a [0], a[-1] = a[-1], a[0]
    return a
n = int(input('m = '))
a = list(map(int, input('В одну строку через пробел').split(maxsplit = n)))
print(a)
print(func1(a))


