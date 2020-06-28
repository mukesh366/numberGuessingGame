

import random

winning_number=random.randint(1,100)
guess=1
game_over=False
number= int(input("Please enter an number between 1-100:         "))


while not game_over:
    if number==winning_number:
        print(f"Congratulation you Win!!!,    and you guess this game in {guess} times")
        game_over=True
    else:
        if number> winning_number:
            print("Too High")
            guess=guess+1
            number=int(input("Please Guess Again      "))
        else:
            print("Too Low")
            guess=guess+1
            number=int(input("Please Guess Again      "))
            
     
