import random
import tkinter as tk 
from tkinter import messagebox

window = tk.Tk()
window.title("Rock Paper Scissors Game")


score_label = tk.Label(window, text="Score: 0")
score_label.pack()


user_score = 0
computer_score = 0
draw_score = 0


def update_score(result):
    global user_score, computer_score, draw_score
    if result == "You win!":
        user_score += 1
    elif result == "Computer wins!":
        computer_score += 1
    else:
        draw_score += 1
    score_label.config(text=f"Score: {user_score} (You) - {computer_score} (Computer) - {draw_score} (Draw)")



def play_game(user_choice):
    choices = ["rock","paper","scissors"]
    computer_choice = random.choice(choices)


    if user_choice == computer_choice:
        result = "It's draw!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        result = "You win!"
    else:
        result = "Computer wins!"
    
    update_score(result)
    messagebox.showinfo("Result",f"You choose {user_choice}. \nComputer chose {computer_choice}.\n\n{result}")



label = tk.Label(window, text="Choose your move:")
label.pack()

rock_button = tk.Button(window, text="Rock", command=lambda: play_game("rock"))
rock_button.pack()

paper_button = tk.Button(window, text="Paper", command=lambda: play_game("paper"))
paper_button.pack()

scissors_button = tk.Button(window, text="Scissors", command=lambda: play_game("scissors"))
scissors_button.pack()


window.mainloop()