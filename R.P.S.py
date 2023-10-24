import random
print("**********Welcome to R.P.S Game**********")
user_choice=0
computer_choice=0
tie=0
name = input("Enter your Name: ")
print("""
Game Rules:
1. Paper vs Rock ---> Paper
2. Rock vs Scissors ---> Rock
3. Scissors vs Paper ---> Scissors""")
while True:
    print("**************")
    print("""Choices are:
    1.Rock
    2.Papers
    3.Scissors""")
    print("**************")
    choice = int(input("Enter your choice from 1-3: "))
    print()
    while choice>3 or choice<1:
        choice = int(input("Enter a valid input"))

    if choice==1:
        user_choice="Rock"
    elif choice==2:
        user_choice="Paper"
    else:
        user_choice="Scissors"

    print("The user,s choice is",user_choice)
    print("Now it is computer turn ")

    computer =random.randint(1,3)

    if computer==1:
        comp_choice="Rock"
    elif computer==2:
        comp_choice="Paper"
    else:
        comp_choice="Scissors"
    print("The computer choice is",comp_choice)

    if ((user_choice=="Paper" and comp_choice=="Rock")or(user_choice=="Rock" and comp_choice=="Paper")):
        print("Paper Wins")
        result="Paper"
    elif ((user_choice=="Paper" and comp_choice=="Scissors")or(user_choice=="Scissors" and comp_choice=="Paper")):
        print("Scissors Wins")
        result="Scissors"
    elif (user_choice==comp_choice):
        print("It,s a Tie")
        result="Tie"
    else:
        print("Rock Wins")
        result="Rock"
    print("**********")
    if result == "Tie":
        print("Tie")
    elif result == comp_choice:
        print("Computer Wins")
    elif result == user_choice:
        print("user,s Wins")
    repeat=input("Do you want to play again? ")
    if repeat =="no":
        break
print("Thanks for playing R.P.S Game ")
