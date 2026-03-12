import tkinter as tk
from tkinter import messagebox

app = tk.Tk()
app.title("Daily Task List")
app.geometry("420x520")
app.configure(bg="#8E977D")

my_tasks = []

def add_new_task():
    user_text = entry_box.get().strip()

    if user_text == "":
        messagebox.showinfo("Oops", "Please type a task first ")
        return

    my_tasks.append(user_text)
    task_list.insert(tk.END, user_text)
    entry_box.delete(0, tk.END)


def remove_task():
    selected_item = task_list.curselection()

    if not selected_item:
        messagebox.showinfo("Oops", "Select a task to remove")
        return

    index = selected_item[0]
    task_list.delete(index)
    my_tasks.pop(index)


def complete_task():
    selected_item = task_list.curselection()

    if not selected_item:
        messagebox.showinfo("Oops", "Select a task first")
        return

    index = selected_item[0]
    task_list.itemconfig(index, fg="gray")
    task_list.itemconfig(index, selectforeground="gray")


heading = tk.Label(app, text="My Daily Tasks", font=("Verdana", 18, "bold"), bg="#AEB784")
heading.pack(pady=15)

entry_box = tk.Entry(app, font=("Verdana", 13))
entry_box.pack(pady=8, ipadx=60, ipady=6)

add_btn = tk.Button(app, text="Add Task", width=18, command=add_new_task)
add_btn.pack(pady=5)

task_list = tk.Listbox(app, width=35, height=13, font=("Verdana", 12))
task_list.pack(pady=15)

done_btn = tk.Button(app, text="Mark as Done", width=18, command=complete_task)
done_btn.pack(pady=5)

delete_btn = tk.Button(app, text="Delete Task", width=18, command=remove_task)
delete_btn.pack(pady=5)

app.mainloop()