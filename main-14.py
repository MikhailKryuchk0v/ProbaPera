import csv
from typing import Iterable, Callable
# 8 вариант

# Реализация собственной функции фильтрации последовательности элементов по заданному предикату(условию)
def my_filter(it: Iterable, predicate: Callable[[any], bool]) -> Iterable:
    return [i for i in it if predicate(i)]


# Реализация собственной функции подсчета кол-ва элеметов в последовательности
def my_count(it: Iterable) -> int:
    count = 0
    return [count := count + 1 for _ in it][-1]


# Открываем файл с данными в формате csv
with open('StudentsPerformance 14.csv', 'r') as f:
    # Инициализируем csv reader
    reader = csv.DictReader(f)
    # Считываем всех студентов из csv
    students = [s for s in reader]
    # Фильтруем студентов согласно условию задачи
    coursed_males = my_filter(students, lambda s: s['gender'] == 'male' and s['test preparation course'] == 'completed')
    # Выводим ответ - кол-во отфильтрованных элеметов (соответствующих заданному условию)
    print(my_count(coursed_males))
    pass
