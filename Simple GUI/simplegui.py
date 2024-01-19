from tkinter import *
root = Tk()
hello = Label(root, text='hello')
hello.grid(row=0,column=0)
goodbye = Label(root, text='goodbye')
goodbye.grid(row=1, column=0)
def been_clicked():
    print('click')

btn = Button(root, text='Click me', command=been_clicked)
btn.grid(row=2, column=0)

hello.config(text='hello')
ent = Entry(root)
ent.grid(row=3,column=0)

root.resizable(width=False, height=False)
