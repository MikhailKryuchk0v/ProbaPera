#TASK2
import math
x = int(input("Введите переменную Х:"))
t = int(input("Введите переменную t:"))
z = ((9*math.pi*t+10*math.cos(x)) / (math.sqrt(t)-math.fabs(math.sin(t))))*math.pow(math.e,x)
print("z = {0:.2f}".format(z))
