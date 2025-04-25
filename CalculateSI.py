from tkinter import*
root=Tk()
root.title("CALCULTE SI AND PI")
def SI():
    result.delete(0,END)
    p=int(e1.get())
    r=int(e2.get())
    t=int(e3.get())
    si=(p*r*t)/100
    result.insert(0,si)
def CI():
    result.delete(0,END)
    p=int(e1.get())
    r=int(e2.get())
    t=int(e3.get())
    si=(p*r*t)/100
    ci=p+si
    result.insert(0,ci)

result=Entry(root,font=("calibri",20,"bold"),bg="#ff5733",fg="Blue",bd=15)
result.grid(columnspan=2)
l1=Label(root,text="PA",font=("calibri",20,"bold"),fg="red")
l1.grid(row=1,column=0)
l2=Label(root,text="RATE",font=("calibri",20,"bold"),fg="red")
l2.grid(row=2,column=0)
l3=Label(root,text="TIME",font=("calibri",20,"bold"),fg="red")
l3.grid(row=3,column=0)
e1=Entry(root,font=("calibri",20,"bold"),fg="Blue",bd=15,width=14)
e1.grid(row=1,column=1)
e2=Entry(root,font=("calibri",20,"bold"),fg="Blue",bd=15,width=14)
e2.grid(row=2,column=1)
e3=Entry(root,font=("calibri",20,"bold"),fg="Blue",bd=15,width=14)
e3.grid(row=3,column=1)
b1=Button(root,text="SI",font=("calibri",20,"bold"),fg="Blue",bg="Pink",bd=13,width=4,command=SI)
b1.grid(row=5,column=0)
b2=Button(root,text="CI",font=("calibri",20,"bold"),fg="Blue",bg="Pink",bd=13,width=4,command=CI)
b2.grid(row=5,column=1)
root.mainloop()
