from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.ttk import Combobox
# 8 var
title = 'task10'

root = Tk()  # создаем корневой объект - окно
root.title(title)  # устанавливаем заголовок окна
root.geometry("1200x600")  # устанавливаем размеры окна

for c in range(3):
    root.rowconfigure(index=c, weight=1)
    root.columnconfigure(index=c, weight=1)

objects = []


def calc():
    try:
        op1 = float(objects[0][0].get())
        op2 = float(objects[0][2].get())
        op = objects[0][1].get()
        if op == '+':
            objects[0][-1]['text'] = op1 + op2
        elif op == '-':
            objects[0][-1]['text'] = op1 - op2
        elif op == '*':
            objects[0][-1]['text'] = op1 * op2
        elif op == '/':
            objects[0][-1]['text'] = op1 / op2
        else:
            objects[0][-1]['text'] = 'Bad command'
    except ZeroDivisionError:
        objects[0][-1]['text'] = 'Zero division'
    except ValueError:
        objects[0][-1]['text'] = 'Bad input'


states = [0, 0, 0]


def c1():
    states[0] = 1 - states[0]


def c2():
    states[1] = 1 - states[1]


def c3():
    states[2] = 1 - states[2]


def check():
    if states[0]:
        showinfo(title="Info", message="You selected first checkbox")
    elif states[1]:
        showinfo(title="Info", message="You selected second checkbox")
    elif states[2]:
        showinfo(title="Info", message="You selected third checkbox")
    else:
        showinfo(title="Info", message="You selected nothing")



contents = [
    [
        lambda x: Entry(x, validate='key'),
        lambda x: Combobox(x, values=['+', '-', '*', '/']),
        lambda x: Entry(x),
        lambda x: Button(x, text='Calc', command=calc),
        lambda x: Label(x, text='No result'),
    ],
    [
        lambda x: Checkbutton(x, text='First', command=c1),
        lambda x: Checkbutton(x, text='Second', command=c2),
        lambda x: Checkbutton(x, text='Third', command=c3),
        lambda x: Button(x, text='Check', command=check),
    ]
]
for c in range(2):
    frame = Frame(borderwidth=1, relief=SOLID)
    frame.grid(row=0, column=c, rowspan=3, padx=8, pady=8, sticky=NSEW)

    for i in range(3):
        frame.rowconfigure(index=i, weight=1)
        frame.columnconfigure(index=i, weight=1)

    objects.append([])
    for i, e in enumerate(contents[c]):
        objects[c].append(e(frame))
        objects[c][i].grid(row=i, column=0, columnspan=3)

frame = Frame(borderwidth=1, relief=SOLID)
frame.grid(row=0, column=2, rowspan=3, padx=8, pady=8, sticky=NSEW)
Text(frame, width=15).pack(fill=BOTH, expand=1)

root.mainloop()
