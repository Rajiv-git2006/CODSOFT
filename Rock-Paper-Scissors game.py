import random

print("Welcome to rock-paper-scissors game!")

options = ["rock","paper","scissors"]
user_score = 0
computer_score = 0

while True:
    print("\nType 'rock', 'paper', or 'scissors' (or 'exit' to quit)")
    user_choice = input("\nYour choice: ").lower()

    if user_choice  == "exit":
        print("\nThanks for playing!")
        print("\nYour Final Score: ",user_score,"\nComputer Score:",computer_score)
        break

    if user_choice not in options:
        print("Invalid option. Try again")
        continue

    computer_choice = random.choice(options)
    print("Computer chose: ",computer_choice)

    if user_choice == computer_choice:
        print("\nIt is a tie!")
        print("Your Score: ",user_score,"\nComputer Score: ",computer_score)

    elif((user_choice == "rock" and computer_choice == "scissors") or
         (user_choice =="scissors" and computer_choice == "paper") or
         (user_choice == "paper" and computer_choice == "rock")):
        print("\nYou win!")
        user_score += 1
        print("Your Score: ",user_score,"\nComputer Score: ",computer_score)
    else:
        print("\nYou lose!")
        computer_score += 1
        print("\nYour Score: ",user_score,"\nComputer Score: ",computer_score)