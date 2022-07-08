print("Welcome to the rollercoaster!!")
ht = int(input("What is your height in cms?"))

if ht>=120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age<12:
        print("Your ticket price is 5$")
    elif 12<=age<18:
        print("Your ticket price is 7$")  
    else:
        print("Your ticket price is 12$")           
else:
    print("Sorry you have to grow taller before you can ride.")
