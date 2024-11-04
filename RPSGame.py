import random


class RPSGame:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.user_score = 0
        self.computer_score = 0

    def play_round(self, user_choice):
        computer_choice = random.choice(self.choices)
        if user_choice == computer_choice:
            return "It's a tie!", computer_choice
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
                (user_choice == 'paper' and computer_choice == 'rock') or \
                (user_choice == 'scissors' and computer_choice == 'paper'):
            self.user_score += 1
            return "You win!", computer_choice
        else:
            self.computer_score += 1
            return "You lose!", computer_choice

    def reset_scores(self):
        self.user_score = 0
        self.computer_score = 0
