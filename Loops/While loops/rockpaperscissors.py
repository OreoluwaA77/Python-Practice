
import random
print("Welcome to my game of Rock, Paper Scissors!")




while True:

    computer_play=(random.choice(['rock','paper','scissors']))

    user_play=str(input("Enter a choice (rock, paper, scissors):"))

    if user_play=='done':
        print ("Well played!")
        break

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

    print("Opponent played",computer_play)
    new_game=str(input("Do you want to play another game? [Yes/No]"))  
    if new_game=='no':
        print("Well played")
        break