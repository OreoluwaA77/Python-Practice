#Write a function calculate_total(price, tax=0.05, discount=0) that calculates the total 
# #price after applying tax and discount. 


def total_price (price, tax=0.05, discount=0):
    print(price + (price*tax) - discount)

total_price(10, tax=0.2)

#Create a function introduce(name, age, profession="Student") and call it using all three argument types. 

def introduce(name, age, profession="Student"):
    print(name, age, profession)

introduce(name="Dara", age=13, profession="Teacher")
introduce("dara", 13,"engineer" )
introduce("Dara", 10)    
introduce("Dara", age=79)