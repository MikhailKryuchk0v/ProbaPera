from typing import List, Any
#8 вариант

# Считываем матрицу порядка n из консоли
def il(n: int) -> List[List[float]]:
    arr = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(float(input(f'Enter element [{i}][{j}]: ')))
        arr.append(row)
    return arr


# Выводим результирующую матрицу
def o(arr: List[List[Any]]):
    print('Result: ')
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end='\t')
        print()


# Решаем задачу
def s(arr: List[List[float]]) -> List[List[float]]:
    k = int(input('Enter k: '))
    # Диагональный элемент строки k
    d_k = arr[k][k]
    # Делим каждый элемент строки k на диагональный элемент d_k
    arr[k] = [e / d_k for e in arr[k]]
    return arr


o(s(il(int(input('Enter array order n: ')))))
