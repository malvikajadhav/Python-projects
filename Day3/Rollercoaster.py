print("Welcome to the rollercoaster!!")
ht = int(input("What is your height in cms?"))

if ht>=120:
    print("You can ride the rollercoaster!")
    ticket = 0
    age = int(input("What is your age?"))
    if age<12:
        ticket = 5
    elif 12<=age<18:
        ticket = 7 
    elif age>=45 and age<=55:
        ticket = 0
    else:
        ticket = 12
    answer = input("Do you want to buy the photos at the gift shop? Enter Yes or No")
    if answer == "Yes":
        print(f"Your total bill is {ticket + 3}$")
    else:
        print(f"Your total bill is {ticket}$")
else:
    print("Sorry you have to grow taller before you can ride.")
    
