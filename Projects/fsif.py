import random
answer=(random.randint(1,100))
count=0
print("Welcome to guess the number")
print("Im thinking of a number between 1-100. Can you guess what it is?")

while True:
    number=int(input("Enter your guess"))
    if number>answer:
        count=count+1
        print("Too high!")
    elif number<answer:
        count=count+1
        print("Too low!")
    elif number == answer:
        print("Congratulations! You have correctly guessed the number",answer)
        break

