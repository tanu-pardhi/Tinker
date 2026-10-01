import tkinter as t
wd=t.Tk()
def clicked():
    n=name.get()
    lastL.config(text="Welcome : "+str(n))

wd.geometry("300x450")
wd.title("Calculator")
l=t.Label(text="Developed By Tanushree ")
nlable=t.Label(text="Enter Name : ")

name=t.Entry(wd)
name.place(x=110,y=40)
b=t.Button(wd,text="Submit",command=clicked)
lastL=t.Label(text="Welcome : ")
lastL.place(x=100,y=90)
nlable.place(x=30,y=40)
l.place(x=100,y=10)
b.place(x=110,y=70)
wd.mainloop()