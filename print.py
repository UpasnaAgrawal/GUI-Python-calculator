
from tkinter import *
import math

def btnClick(number):
    global val
    val = val + str(number)
    Data.set(val)

def btnClear():
    global val
    val = ""
    Data.set("")

def btnEquals():
    global val
    try:
        result = str(eval(val))
        Data.set(result)
        val = result  # Store the result for further calculations
    except Exception as e:
        Data.set("Error")
        val = ""

def btnBackspace():
    global val
    val = val[:-1]  # Remove the last character
    Data.set(val)

def btnDecimal():
    global val
    if '.' not in val:  # Prevent multiple decimals
        val += '.'
        Data.set(val)

def btnSquare():
    global val
    try:
        result = str(float(val) ** 2)
        Data.set(result)
        val = result
    except Exception as e:
        Data.set("Error")
        val = ""

def btnSquareRoot():
    global val
    try:
        result = str(math.sqrt(float(val)))
        Data.set(result)
        val = result
    except Exception as e:
        Data.set("Error")
        val = ""

root = Tk()
root.title("My Calculator")
root.geometry("400x500+500+200") 
val = ""

Data = StringVar()

display = Entry(root, textvariable=Data, bd=29, justify="right", bg="powder blue",font=("arial", 20))
display.grid(row=0, columnspan=4)

btn7 = Button(root, text="7", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick(7))
btn7.grid(row=1, column=0)
btn8 = Button(root, text="8", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick(8))
btn8.grid(row=1, column=1)
btn9 = Button(root, text="9", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick(9))
btn9.grid(row=1, column=2)
btn_add = Button(root, text="+", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick("+"))
btn_add.grid(row=1, column=3)

btn4 = Button(root, text="4", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick(4))
btn4.grid(row=2, column=0)
btn5 = Button(root, text="5", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick(5))
btn5.grid(row=2, column=1)
btn6 = Button(root, text="6", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick(6))
btn6.grid(row=2, column=2)
btn_sub = Button(root, text="-", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick("-"))
btn_sub.grid(row=2, column=3)

btn1 = Button(root, text="1", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick(1))
btn1.grid(row=3, column=0)
btn2 = Button(root, text="2", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick(2))
btn2.grid(row=3, column=1)
btn3 = Button(root, text="3", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick(3))
btn3.grid(row=3, column=2)
btn_mul = Button(root, text=" *", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick("*"))
btn_mul.grid(row=3, column=3)

btn_clear = Button(root, text="C", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=btnClear)
btn_clear.grid(row=4, column=0)
btn_0 = Button(root, text="0", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick(0))
btn_0.grid(row=4, column=1)
btn_equal = Button(root, text="=", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=btnEquals)
btn_equal.grid(row=4, column=2)
btn_div = Button(root, text="/", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick("/"))
btn_div.grid(row=4, column=3)

btn_dec = Button(root, text=".", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=btnDecimal)
btn_dec.grid(row=5, column=0)
btn_backspace = Button(root, text="Back", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=btnBackspace)
btn_backspace.grid(row=5, column=1)
btn_sqr = Button(root, text="Sqr", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=btnSquare)
btn_sqr.grid(row=5, column=2)
btn_sqrt = Button(root, text="Sqrt", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=btnSquareRoot)
btn_sqrt.grid(row=5, column=3)

root.mainloop()

