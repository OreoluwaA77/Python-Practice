km_travelled=float(input("Please entrer the kilometres you covered"))
if km_travelled<=10:
  print("Amount payable is $", km_travelled*11)
elif 100>=km_travelled>10:
  print("Amount payable is $", (km_travelled-km_travelled+10)*11 +(km_travelled-10)*10)