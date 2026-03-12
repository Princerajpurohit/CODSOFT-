import tkinter as tk
import random
import string

def password_Ganerate():
    length = int(length_entry.get())

    if length < 4 or length > 15:
        result_label.config(text="Length must be 4-15")
        return

    letter = random.choice(string.ascii_letters)
    number = random.choice(string.digits)


    other_chars = string.ascii_letters + string.digits 
    rest = "".join(random.choice(other_chars) for i in range(length-3))

    password_list = list(letter + number + rest)
    random.shuffle(password_list)

    password = "".join(password_list)

    result_label.config(text=password)

root = tk.Tk()
root.title("Password Generator")
root.geometry("300x200")
root.configure(bg="#003049")

title = tk.Label(root, text="Password Generator", font=("Arial",14),bg="#D62828",fg="black")
title.pack(pady=10)

length_label = tk.Label(root, text="Enter Length (4-15)")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack(pady=5)

generate_btn = tk.Button(root, text="Generate Password", command=password_Ganerate,bg="#F77F00",fg="black")
generate_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial",12))
result_label.pack(pady=10)

root.mainloop()