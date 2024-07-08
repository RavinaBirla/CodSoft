# Task-4 :Rock-Paper-Scissor Game

import random
comchoice=["Rock","Paper","Scissor"]

while True:
    usercount,comcount=0,0
    print(".........Rock-Paper-Scissors Game.........")
    # asked to user that how many time he/she want to play
    n=int(input("How many times you play "))
    i=0
    while i<n:
        i+=1
        print(f"Enter your choice for round {i}")
        print("1: Rock \n2: Paper \n3: Scissor")
        # User choice
        uch=int(input())
        if uch==1:
            userch="Rock"
            print("you choose Rock")
        elif uch==2:
            userch="Paper"
            print("you choose Paper")
        elif uch==3:
            userch="Scissor"
            print("you choose Scissor")
        else:
            print("Invalid choice")
            break
        # computer random choice
        comch=random.choice(comchoice)
        print("Computer choose ",comch) 
        if userch==comch:
            usercount+=1
            comcount+=1
            print("this round is tie")
        elif (userch=="Rock" and comch=="Scissor") or (userch=="Scissor" and comch=="Paper") or (userch=="Paper" and comch=="Rock"):
            usercount+=1
            print("User win this round")
        else:
            comcount+=1
            print("Computer win this round")
    if usercount>comcount:
        print(f"User score is {usercount} and computer score is {comcount}")
        print("...User is Winner...")
    elif comcount>usercount:
        print(f"User score is {usercount} and computer score is {comcount}")
        print("...Computer is Winner...")
    else:
        print(f"User score is {usercount} and computer score is {comcount}")
        print("Game is tie")
    ch=input("if you want to play again press Y otherwise N ")
    if ch=="Y" or ch=="y":
        continue
    else :
        break                       
