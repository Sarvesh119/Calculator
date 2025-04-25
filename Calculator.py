#      CALCULATOR
import tkinter
from tkinter import *
from tkinter import messagebox
r=Tk()
r.geometry("420x500")
r.configure(bg="lightyellow")
r.title("CALCULATOR")
r.resizable(0,0)
expression=" "
equation=StringVar()
expression_field=Entry(r,textvariable=equation,font=("bold",25),bd=8)
expression_field.place(x=20,y=50,width=360, height=90)
def press(num):
    global expression
    expression=expression+str(num)
    equation.set(expression)
def equalpress():
    try:
        global expression
        total =str(eval(expression))
        equation.set(total)
        expression= " "
    except:
        equation.set("error")
        expression= " "
def clear():
     global expression
     expression= " "
     equation.set(" ")
l1=Label(r,text="CALCULATOR  MADE BY SARVESH MISHRA",font=("bold",15),bg="lightyellow")
l1.pack()
btn1=Button(r,text="7",font=("bold",20),command=lambda:press(7),fg="white",bg="Blue")
btn1.place(x=10,y=180,width=80,height=80)
btn2=Button(r,text="8",font=("bold",20),command=lambda:press(8),fg="white",bg="Blue")
btn2.place(x=90,y=180,width=80,height=80)
btn3=Button(r,text="9",font=("bold",20),command=lambda:press(9),fg="white",bg="Blue")
btn3.place(x=170,y=180,width=80,height=80)
btn3=Button(r,text="*",font=("bold",20),command=lambda:press("*"),fg="white",bg="Blue")
btn3.place(x=250,y=180,width=80,height=80)
btn3=Button(r,text="exit",font=("bold",20),command=lambda:exit(),fg="white",bg="Blue")
btn3.place(x=330,y=180,width=80,height=80)

btn4=Button(r,text="4",font=("bold",20),command=lambda:press(4),fg="white",bg="Blue")
btn4.place(x=10,y=260,width=80,height=80)
btn5=Button(r,text="5",font=("bold",20),command=lambda:press(5),fg="white",bg="Blue")
btn5.place(x=90,y=260,width=80,height=80)
btn6=Button(r,text="6",font=("bold",20),command=lambda:press(6),fg="white",bg="Blue")
btn6.place(x=170,y=260,width=80,height=80)
btn3=Button(r,text="-",font=("bold",20),command=lambda:press("-"),fg="white",bg="Blue")
btn3.place(x=250,y=260,width=80,height=80)
btn3=Button(r,text="clear",font=("bold",20),command=clear,fg="white",bg="Blue")
btn3.place(x=330,y=260,width=80,height=80)

btn7=Button(r,text="1",font=("bold",20),command=lambda:press(1),fg="white",bg="Blue")
btn7.place(x=10,y=340,width=80,height=80)
btn8=Button(r,text="2",font=("bold",20),command=lambda:press(2),fg="white",bg="Blue")
btn8.place(x=90,y=340,width=80,height=80)
btn9=Button(r,text="3",font=("bold",20),command=lambda:press(3),fg="white",bg="Blue")
btn9.place(x=170,y=340,width=80,height=80)
btn3=Button(r,text="+",font=("bold",20),command=lambda:press("+"),fg="white",bg="Blue")
btn3.place(x=250,y=340,width=80,height=80)
btn3=Button(r,text="%",font=("bold",20),command=lambda:press("%"),fg="white",bg="Blue")
btn3.place(x=330,y=340,width=80,height=80)

btn9=Button(r,text="00",font=("bold",20),command=lambda:press(00),fg="white",bg="Blue")
btn9.place(x=10,y=420,width=80,height=80)
btn9=Button(r,text="0",font=("bold",20),command=lambda:press(0),fg="white",bg="Blue")
btn9.place(x=90,y=420,width=80,height=80)
btn9=Button(r,text=".",font=("bold",30),command=lambda:press("."),fg="white",bg="Blue")
btn9.place(x=170,y=420,width=80,height=80)
btn3=Button(r,text="=",font=("bold",20),command=equalpress,fg="white",bg="Blue")
btn3.place(x=250,y=420,width=80,height=80)
btn3=Button(r,text="÷",font=("bold",20),command=lambda:press("/"),fg="white",bg="Blue")
btn3.place(x=330,y=420,width=80,height=80)
mainloop()
