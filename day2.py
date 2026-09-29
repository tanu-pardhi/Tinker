import tkinter as t

wd=t.Tk()
wd.title("Calculator")
wd.geometry("300x450")
def clicked():
    print("Button Clicked")
lb=t.Label(wd,text="this is day 1")
b=t.Button(wd,text="submit",command=clicked)
lb.pack()
b.pack()

wd.mainloop()