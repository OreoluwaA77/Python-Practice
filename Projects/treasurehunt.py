#import random for coordinates 
#Import math too 
#Ask user for coordinates 
#Use formula to work out distance between player guess and computer guess 
#Show result of formula  
#categorise into close far very close 
#End game on two conditions win or 5 attempts used  
#Add up total wins and losses throughout the game until user decides to stop playing 

import random 
import math 
count=0

print("Welcome to the Treasure Hunt Simulation!") 
print("The treasure is hidden on a 10x10 grid. You have 5 attempts to find it.")

while True:
    x_coordinate=(random.randint(1,10))
    y_coordinate=(random.randint(1,10))

    x_user_guess=int(input("Enter your x coordinate (x):"))
    y_user_guess=int(input("Enter your y coordinate (y):"))

    count=count + 1

    distance= round(math.sqrt((x_user_guess-x_coordinate)**2 + (y_user_guess-y_coordinate)**2))

    if count==5:
        print("You've used up all your guesses :( Better luck next time!" "The coordinates where", x_coordinate,"," ,y_coordinate)
        break
    
    if distance ==0:
        print("Welldone!! You found the treasure!")
        break

    if distance <= 2:
        print("You're very close! Keep going! Only",distance,"metres away")

    elif distance<=5:
        print("Close! Keep searching! Only",distance,"metres away")

    else:
        print("Your far! Try somewhere new, Only",distance,"metres away")

