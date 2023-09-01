import tkinter as tk
import random

class Rock_Paper_Scissors_Game:
    def __init__(self, root):
        self.root = root
        self.root.title("ROCK-PAPER-SCISSORS GAME")

        self.User_Score = 0
        self.Computer_Score = 0

        self.Choices = ["rock", "paper", "scissors"]

        self.Label = tk.Label(root, text="Choose anyone: Rock, Paper, or Scissors")
        self.Label.pack()

        self.Button_Frame = tk.Frame(root)
        self.Button_Frame.pack()

        self.User_Choice = tk.StringVar()

        for choice in self.Choices:
            Button = tk.Button(self.Button_Frame, text=choice.capitalize(), command=lambda choice=choice: self.Play(choice))
            Button.pack(side=tk.LEFT)

        self.Result_Label = tk.Label(root, text="", padx=20)
        self.Result_Label.pack()

        self.Score_Label = tk.Label(root, text="Your Score is: 0   Computer's Score is: 0")
        self.Score_Label.pack()

    def Play(self, User_Choice):
        Computer_Choice = random.choice(self.Choices)

        Result = self.Determine_Winner(User_Choice, Computer_Choice)
        if Result == "tie":
            Result_Text = "It's a Tie!!"

        elif Result == "user":
            Result_Text = "You Win!!"
            self.User_Score +=1

        else:
            Result_Text = "Computer Wins!!"
            self.Computer_Score +=1

        self.Result_Label.config(text=f"Computer Choose {Computer_Choice.capitalize()}. {Result_Text}")
        self.Update_Score_Label()

    def Determine_Winner(self, User_Choice, Computer_Choice):
        if User_Choice == Computer_Choice:
            return "tie"
        elif (User_Choice == "rock" and Computer_Choice == "scissors") or \
             (User_Choice == "scissors" and Computer_Choice == "paper") or \
             (User_Choice == "paper" and Computer_Choice == "rock"):
            return "user"
        
        else:
            return "computer"
        
    def Update_Score_Label(self):
        self.Score_Label.config(text=f"Your Score is: {self.User_Score} Computer's Score is: {self.Computer_Score}")

root = tk.Tk()
Game = Rock_Paper_Scissors_Game(root)
root.mainloop()