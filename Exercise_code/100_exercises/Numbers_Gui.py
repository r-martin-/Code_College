import sys
from tkinter import *

"""
simple program which uses a gui
asks the user if the want to add,subtract,multiply or divide the entered numbers
"""

def getInput():
    
    myNumber1 = number1.get()
    myNumber2 = number2.get()
    mySymbol = symbol.get()

    
    if mySymbol in '+':
        add(myNumber1,myNumber2)
        
    elif mySymbol in '-':
        sub(myNumber1,myNumber2)
        
    elif mySymbol in '*':
        multiply(myNumber1,myNumber2)
        
    else:
        divide(myNumber1,myNumber2)

    
    return

def add(num1,num2):
    ans =0

    ans = num1 +num2
    print("addition is",ans)
    return

def sub(num1,num2):
    ans = 0
    ans = num1 - num2
    print(ans)
    return

def multiply(num1,num2):
    ans = 0
    ans = num1 * num2
    print(ans)
    return

def divide(num1,num2):
    ans = 0
    ans = num1 / num2
    print(ans)
    return




myGui = Tk()
number1 = IntVar()
number2 = IntVar()
symbol = StringVar()


myGui.geometry("400x400")
myGui.title( "calculator")


myGui = Label(text = "enter number 1, then hit submit").pack()
myEntry = Entry(text= number1).pack()
myButton = Button(text= "submit",command = getInput).pack()


myGui = Label(text = "enter number 2, then hit submit").pack()
myEntry2 = Entry(text = number2).pack()
myButton1 = Button(text= "submit",command = getInput).pack()

myGui = Label(text = "select +,-,* or / to get your answer to the sum").pack()
myEntry3 = Entry(text=symbol).pack()
myButton3 = Button(text= "submit",command = getInput).pack()



mainloop()
