#Tkinter_Calculator

from tkinter import *
window=Tk()
window.geometry("312x324")
window.title("Swapnil's Calculator")
def click(item):
    global expression
    expression=expression+str(item)
    input_text.set(expression)
def clr():
    global expression
    expression=""
    input_text.set("")
def equal():
    global expression
    result=str(eval(expression))
    input_text.set(result)
    expression=""
expression=""
input_text=StringVar()
#FRAME
frame=Frame(window,width=312,height=50,bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
frame.pack(side=TOP)
field=Entry(frame,textvariable=input_text,width=50,bd=0,justify=RIGHT)
field.grid(row=0,column=0)
field.pack(ipady=10)
btns=Frame(window,width=312,height=272.5)
btns.pack()
# first row
clear = Button(btns, text = "C", fg = "black", width = 32, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: clr()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
divide = Button(btns, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)
# second row
seven = Button(btns, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
eight = Button(btns, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
nine = Button(btns, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
multiply = Button(btns, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
 
# third row
four = Button(btns, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
five = Button(btns, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
six = Button(btns, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
minus = Button(btns, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
 
# fourth row
one = Button(btns, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
two = Button(btns, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
three = Button(btns, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
plus = Button(btns, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)
 
# fourth row
zero = Button(btns, text = "0", fg = "black", width = 21, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
point = Button(btns, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
equals = Button(btns, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: equal()).grid(row = 4, column = 3, padx = 1, pady = 1)
window.mainloop()