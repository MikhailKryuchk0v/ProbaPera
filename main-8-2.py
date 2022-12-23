from typing import List, Any
# 8 вариант

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
    # Транспонируем матрицу arr - отображаем элемент arr[i][j] в arr[j][i]
    return [[arr[j][i] for j in range(len(arr[i]))] for i in range(len(arr))]


o(s(il(int(input('Enter array order n: ')))))
