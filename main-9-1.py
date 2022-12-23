from typing import List, Any
# 8 var
i_name = 'vvod.txt'
o_name = 'vivod.txt'


# Считываем матрицу порядка n из консоли
def il(n: int) -> List[List[float]]:
    arr = []
    for i in range(n):
        arr.append([float(e) for e in fi.readline().split()])
    return arr


# Выводим результирующую матрицу
def o(arr: List[List[Any]]):
    fo.write('Result: \n')
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            fo.write(str(arr[i][j]) + '\t')
        fo.write('\n')


# Решаем задачу
def s(arr: List[List[float]]) -> List[List[float]]:
    k = int(fi.read())
    # Диагональный элемент строки k
    d_k = arr[k][k]
    # Делим каждый элемент строки k на диагональный элемент d_k
    arr[k] = [e / d_k for e in arr[k]]
    return arr


with open(i_name, 'r') as fi, open(o_name, 'w') as fo:
    o(s(il(int(fi.readline()))))
