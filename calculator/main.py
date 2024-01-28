import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title('Calculator')

e = tk.Entry(window, width=9, font=('Calibri', 40) )
e.grid(row=0, column=0, columnspan=4)

num1 = 0
op = ''

def sign():
    current = e.get()
    e.delete(0, END)
    e.insert(0, float(current) * (-1))

def clear():
    global num1, op
    e.delete(0, END)
    num1 = 0
    op = ''

def btn_click(num):
    current = e.get()
    e.delete(0, END)
    if '.' in current and num=='.':
        e.insert(0, str(current))
    else:
        e.insert(0, str(current) + str(num))

def perform_operation():
    global num1, op
    num2 = e.get()
    e.delete(0, END)

    if op == 'sum':
        res = num1 + float(num2)
    elif op == 'sub':
        res = num1 - float(num2)
    elif op == 'mul':
        res = num1 * float(num2)
    elif op=='per':
        res=(float(num2)/100)*num1
    elif op == 'div':
        if float(num2) != 0:
            res = num1 / float(num2)
        else:
            e.insert(0, "Error")
            return
    res=float(str(res).rstrip('0').rstrip('.'))
    e.insert(0, res)
    num1 = res
    op = ''

def set_operation(operation):
    global num1, op
    num1 = float(e.get())
    op = operation
    e.delete(0, END)

# Defining the buttons
btn_list = [None] * 10
for i in range(10):
    btn_list[i] = tk.Button(text=str(i), font=('Calibri', 24), pady=5, command=lambda i=i: btn_click(i))

btnC = tk.Button(text='C', font=('Calibri', 24), pady=5, command=clear)
btn_plus = tk.Button(text='+', font=('Calibri', 24), pady=5, command=lambda: set_operation('sum'))
btn_per = tk.Button(text='%',  font=('Calibri', 24),pady=5,command=lambda: set_operation('per'))
btn_sub = tk.Button(text='-', font=('Calibri', 24), pady=5, command=lambda: set_operation('sub'))
btn_mul = tk.Button(text='*', font=('Calibri', 24), pady=5, command=lambda: set_operation('mul'))
btn_div = tk.Button(text='/', font=('Calibri', 24), pady=5, command=lambda: set_operation('div'))
btn_dec = tk.Button(text='.', font=('Calibri', 24), pady=5, command=lambda: btn_click('.'))
btn_eq = tk.Button(text='=', font=('Calibri', 24), pady=5, command=perform_operation)
btn_sign = tk.Button(text='+/-', font=('Calibri', 14), pady=5, command=sign)

btnC.grid(row=1, column=0, columnspan=1, sticky='nsew')
btn_sign.grid(row=1, column=1, columnspan=1, sticky='nsew')
btn_div.grid(row=1, column=3, columnspan=1, sticky='nsew')
btn_per.grid(row=1, column=2, columnspan=1, sticky='nsew')
btn_list[7].grid(row=2, column=0, sticky='nsew')
btn_list[8].grid(row=2, column=1, sticky='nsew')
btn_list[9].grid(row=2, column=2, sticky='nsew')
btn_list[4].grid(row=3, column=0, sticky='nsew')
btn_list[5].grid(row=3, column=1, sticky='nsew')
btn_list[6].grid(row=3, column=2, sticky='nsew')
btn_list[1].grid(row=4, column=0, sticky='nsew')
btn_list[2].grid(row=4, column=1, sticky='nsew')
btn_list[3].grid(row=4, column=2, sticky='nsew')
btn_list[0].grid(row=5, column=0, columnspan=2, sticky='nsew')
btn_mul.grid(row=2, column=3, sticky='nsew')
btn_sub.grid(row=3, column=3, sticky='nsew')
btn_plus.grid(row=4, column=3, sticky='nsew')
btn_eq.grid(row=5, column=3, sticky='nsew')
btn_dec.grid(row=5, column=2, sticky='nsew')

window.mainloop()
