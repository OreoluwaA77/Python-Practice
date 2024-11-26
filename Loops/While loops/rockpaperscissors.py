import random
computer_play=(random.choice(['rock','paper','scissors']))
print("Welcome to my game of Rock, Paper Scissors!")

while True:
    user_play=str(input("Enter a choice (rock, paper, scissors):"))
    if user_play=='done':
        print ()

    if user_play=='rock' and computer_play=='rock':
        print("Thats a draw")
        
    elif user_play=='rock' and computer_play=='scissors':
        print("Weldone! You win")
    elif user_play=='rock' and computer_play=='paper':
        print("You lose!")
    elif user_play=='paper' and computer_play=='paper':
        print("Thats a draw!")
    elif user_play=='paper' and computer_play=='rock':
        print("Welldone!You win")
    elif user_play=='paper' and computer_play=='scissors':
        print("You lose!")
    elif user_play=='scissors' and computer_play=='scissors':
        print("Thats a draw!")
    elif user_play=='scissors' and computer_play=='paper':
        print("Welldone! You win")
    elif user_play=='scissors' and computer_play=='rock':
        print("You lose!")
