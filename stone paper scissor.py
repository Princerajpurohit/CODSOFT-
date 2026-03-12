import tkinter as tk
from tkinter import messagebox
import random

def RPS_game(user):

    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)

    if user == computer_choice:
        result = "Match Draw"

    elif (user == "Rock" and computer_choice == "Scissors") or \
         (user == "Paper" and computer_choice == "Rock") or \
         (user == "Scissors" and computer_choice == "Paper"):
        result = "You Won the Game"

    else:
        result = "you lose , computer win !"

    message = f"My Choice : {user}\nComputer Choice : {computer_choice}\n\nResult : {result}"

    messagebox.showinfo("Result: ", message)


window = tk.Tk()
window.title("Rock Paper Scissors Game")
window.geometry("320x280")
window.configure(bg="#2C3E50")
window.resizable(False, False)

title = tk.Label(window, text="Rock Paper Scissors", font=("Arial",14), bg="#2C3E50",fg="white")
title.pack(pady=10)

btn1 = tk.Button(window, text="Rock", width=12, command=lambda: RPS_game("Rock"),bg="#4C3C1D",fg="white")
btn1.pack(pady=5)

btn2 = tk.Button(window, text="Paper", width=12, command=lambda: RPS_game("Paper"),bg="#ECFDF3",fg="black")
btn2.pack(pady=5)

btn3 = tk.Button(window, text="Scissors", width=12, command=lambda: RPS_game("Scissors"),bg="#441A15",fg="white")
btn3.pack(pady=5)

window.mainloop()