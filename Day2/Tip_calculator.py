print("Welcome to tip calculator!!")
bill = float(input("ENter your bill amount:"))
people = int(input("How many people are splitting the bill?"))
tip = input("How much percent tip would you like to leave?")
tip = 1 + (int(tip)/100)
total =  bill * tip
per_person = "{:.2f}".format(round(total/people,2))
print(f"Each person should pay {per_person}")
