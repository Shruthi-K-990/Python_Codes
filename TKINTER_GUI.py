from tkinter import *
root = Tk()
root.title("Welcome to Python Programming")
root.geometry('350x200')
menu = Menu(root)
item = Menu(menu)
item.add_command(label='New')
menu.add_cascade(label='File',menu=item)
root.config(menu=menu)

lbl = Label(root,text="Are you a programmer?")
lbl.grid()
txt = Entry(root,width=10)
txt.grid(column=1,row=0)
def clicked():
    res = "You typed" + txt.get()
    lbl.configure(text=res)
btn = Button(root,text="click me",fg="blue",command=clicked)
btn.grid(column=2,row=0)
root.mainloop()




