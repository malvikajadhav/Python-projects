print("Welcoem to Python Pizzas!!!")
size = input("What size of pizza would you like to order? S, M or L\n")
add_pepperoni = input("Do you want to add pepperoni topping to the pizza? Y or N\n")
bill = 0
if size == "S":
    bill = 15
    if add_pepperoni == 'Y':
        bill +=2
elif size == "M":
    bill = 20
    if add_pepperoni == 'Y':
        bill +=3
else:
    bill = 25
    if add_pepperoni == 'Y':
        bill +=3
extra_cheese = input("Do you want to add extra cheese to the pizza? Y or N\n")
if extra_cheese == 'Y':
    bill+=1
    
print(f"Your final bill amount is {bill}$.")
