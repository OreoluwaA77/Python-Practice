player_name= str(input('please enter your name'))
total_points=float(10)
print("Hello", player_name,"! You have", total_points, "points!")
location=str(input('Where would you like to go.. cave or forest or castle '))

if location=='cave':
    if total_points>=10:
        total_points= total_points + 20  
    print("Welldone",player_name,"you now have", total_points, "!, You found treasure! You now have", total_points)
elif location=='cave':
    if total_points<10:
        total_points=total_points - 5
    print("You encountered a monster and lose 5 points. You now have", total_points)

elif location=='forest':
    if total_points>=5:
        total_points=total_points + 10
    print("Welldone", player_name, "you now have", total_points, "!, You met a wixard who appointed to 10 points. You now have", total_points)

elif location=='forest':
    if total_points<5:
        total_points= total_points - 2
    print("You lost your battle with the wizard and lost two points You now have", total_points)

elif location=='castle':
    if total_points>=15:
        total_points=total_points+25
    print("Welldone", player_name, "you now have", total_points,"!, You have succesfully saved the princess")
    if total_points<15:
        total_points=total_points-10
    print('You were caught by the guards and lost 10 points ypu now have', total_points)

else:
    print("Your total points are", total_points)
