import os, random
from msvcrt import getwch
from RPSfunk import hand

os.system('cls')



keys = ["R", "P", "S", "Q"]
"""
Rock = 0
Paper = 1
Scissors = 2
"""
wins = 0
losses = 0 
ties = 0
turns = 0

while True:
    print("Rock(R), Paper(P), Scissors(S) \nPress Q to exit")
    while True:
        
        choice = getwch().upper()
        if choice in keys:  
            break
        
    os.system('cls')

    ai = random.randint(0,2)
    ai_choice = hand(ai)
    print(f"ai chose:{ai_choice}")
    turns+=1 
    
    if choice == "Q":
        break
    
    if choice == hand(ai):
        print("its a tie")
        ties+=1

    elif choice == "P":  #Paper
        if ai_choice == "R":
            print("you won")
            wins+=1
        else:
            print("you lost")
            losses+=1

    elif choice == "R":
        if hand(ai) == "S":
            print("You win")
            wins+=1
        else:
            print("you lost")
            losses+=1

    elif choice == "S":
        if hand(ai) == "P":
            print("You win")
            wins+=1
        else:
            print("you lost")
            losses+=1


    print(f"wins: {wins} losses{losses} ties{ties} turns{turns}")