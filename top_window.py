from tkinter import *

root = Tk()
root.title('Root Window')
root.geometry('400x400')

btn = Button(text="Click me for another window to pop up!")
btn.pack()
def top_level(top):
    top = Toplevel()
    top.title('Top Level Window')
    top.geometry('200x200')
    l2 = Label(top, bg="#3895d3", fg="white", width=20, text="This is a top level window!")
    l2.pack()
btn.bind("<Button-1>", top_level)
root.mainloop()