from tkinter import *

def add():
    if task_var.get()!="":
        task_list.insert(END, task_var.get())

def remove():
    if task_list.get(ANCHOR):
        task_list.delete(ANCHOR)

root = Tk()

task_var = StringVar()

root.resizable(False,False)
root.title("To-Do List")
root.geometry("400x600")

task_list = Listbox(root, width=25, height=30)
task_list.place(x=15,y=15)

task_entry = Entry(root, text=task_var, width=25)
task_entry.place(x=15,y=550)

add_btn = Button(root, text="Add Task", width=20, height=1, command=add)
add_btn.place(x=220,y=15)

remove_btn = Button(root, text="Remove Task", width=20, height=1, command=remove)
remove_btn.place(x=220,y=55)

root.mainloop()
