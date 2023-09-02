import tkinter as tk
from tkinter import ttk
import random

class Rock_Paper_Scissors_Game:
    def __init__(self, root):
        self.root = root
        self.root.title("ROCK-PAPER-SCISSORS GAME")

        BackGround_Color = "#32f7fa"

        self.root.configure(bg=BackGround_Color)

        self.User_Score = 0
        self.Computer_Score = 0

        self.Choices = ["rock", "paper", "scissors"]
        self.Data = []

        self.Label = tk.Label(root, text="SAY!! ROCK!! PAPER!! SCISSORS!!", font=("Times New Roman", 16, "bold underline"), fg="white", bg=BackGround_Color)
        self.Label.pack(pady=10)

        self.Button_Frame = tk.Frame(root, bg=BackGround_Color)
        self.Button_Frame.pack()

        self.User_Choice = tk.StringVar()

        for choice in self.Choices:
            Button = tk.Button(self.Button_Frame, text=choice.capitalize(), command=lambda choice=choice: self.Play(choice), width=10, font=("Times New Roman", 12, "bold"))
            Button.pack(side=tk.LEFT, padx=10)

        self.Result_Label = tk.Label(root, text="", padx=20, font=("Xenara", 14, "bold"), fg="white", bg=BackGround_Color)
        self.Result_Label.pack(pady=10)

        self.Score_Label = tk.Label(root, text="YOUR SCORE IS: 0   COMPUTER'S SCORE IS: 0", font=("Times New Roman", 12, "bold underline"), fg="white", bg=BackGround_Color)
        self.Score_Label.pack()

        self.Create_Table()

    def Play(self, User_Choice):
        Computer_Choice = random.choice(self.Choices)

        Result = self.Determine_Winner(User_Choice, Computer_Choice)
        if Result == "tie":
            Result_Text = "IT'S A TIE!!"

        elif Result == "user":
            Result_Text = "YOU WIN!!"
            self.User_Score +=1

        else:
            Result_Text = "COMPUTER WINS!!"
            self.Computer_Score +=1

        self.Result_Label.config(text=f"COMPUTER CHOOSE {Computer_Choice.capitalize()}. {Result_Text}", font=("Times New Roman", 14, "bold"))
        self.Update_Score_Label()

        self.Data.append((User_Choice.capitalize(), Computer_Choice.capitalize(), Result_Text))
        self.Update_Table()

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
        self.Score_Label.config(text=f"YOUR SCORE IS: {self.User_Score} COMPUTER'S SCORE IS: {self.Computer_Score}", font=("Times New Roman", 12, "bold"), fg="white")

    def Create_Table(self):
        self.Table_Frame = tk.Frame(self.root, bg="white")
        self.Table_Frame.pack(pady=10)

        self.Table = ttk.Treeview(self.Table_Frame, columns=("user", "computer", "result"), show='headings')
        self.Table.heading("user", text="USER CHOICE", anchor="center")
        self.Table.heading("computer", text="COMPUTER CHOICE", anchor="center")
        self.Table.heading("result", text="RESULT", anchor="center")
        
        self.Table.pack()

    def Update_Table(self):
        for item in self.Table.get_children():
            self.Table.delete(item)
        for data in self.Data:
            self.Table.insert("", "end", values=data)


root = tk.Tk()
root.geometry("700x500")
Game = Rock_Paper_Scissors_Game(root)
root.mainloop()