from tkinter import *
import tkinter.font as font
import random

player_score = 0
computer_score = 0
options = [("rock",0), ("paper", 1), ("scissors",2)]

def computer_wins():
    global computer_score, player_score
    computer_score += 1
    winner_label.config(text = "Computer Wins!!")
    computer_score_label.config(text = "Computer Score: "+ str(computer_score))
    player_score_label.config(text = "Player Score: " + str(player_score))

def player_wins():
    global computer_score, player_score
    player_score += 1
    winner_label.config(text = "You Win!!")
    computer_score_label.config(text = "Computer Score: "+ str(computer_score))
    player_score_label.config(text = "Player Score: " + str(player_score))

def tie():
    global computer_score, player_score
    winner_label.config(text = "It's A Tie!!")
    computer_score_label.config(text = "Computer Score: " + str(computer_score))
    player_score_label.config(text = "Player Score: " + str(player_score))

def player_choice(player_input):
    global player_score, computer_score
    print(player_input)

    computer_input = get_computer_choice()
    print(computer_input)
    player_choice_label.config(text = "You Selected: " + player_input[0])
    computer_choice_label.config(text = "Computer Selected: " + computer_input[0])

    if(player_input == computer_input):
        tie()

    if(player_input[1] == 0):
        if(computer_input[1] == 1):
            computer_wins()
        elif(computer_input[1] == 2):
            player_wins()

    elif(player_input[1] == 1):
        if(computer_input[1] == 0):
            player_wins()
        elif(computer_input[1] == 2):
            computer_wins()

    elif(player_input[1] == 2):
        if(computer_input[1] == 0):
            computer_wins()
        elif(computer_input[1] == 1):
            player_wins()

def get_computer_choice():
    return random.choice(options)

game_window = Tk()
game_window.title("Rock Paper Scissors")

app_font = font.Font(size = 12)

game_title = Label(text = "Rock Paper Scissors", font = font.Font(size = 20), fg = "grey")
game_title.pack()

winner_label = Label(text = "Let's Start the Game...", fg = "green", font = font.Font(size = 13), pady = 8)
winner_label.pack()

input_frame = Frame(game_window)
input_frame.pack

player_options = Label(input_frame, text = "Your Options: ", font = app_font, fg = "grey")

rock_btn = Button(input_frame, text = "Rock", width = 15, bd = 0, bg = "silver", pady = 5, command = lambda: player_choice(options))
rock_btn.grid(row = 1, column = 1, padx = 8, pady = 5)

paper_btn = Button(input_frame, text = "Paper", width = 15, bd = 0, bg = "light blue", pady = 5, command = lambda: player_choice(options))
paper_btn.grid(row = 1, column = 2, padx = 8, pady = 5)

scissors_btn = Button(input_frame, text = "Scissors", width = 15, bd = 0, bg = "pink", pady = 5, command = lambda: player_choice(options))
scissors_btn.grid(row = 1, column = 3, padx = 8, pady = 5)

score_label = Label(input)