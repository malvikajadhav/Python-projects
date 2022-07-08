print("Welcome to love calculator!!")
name = input("What is your name? ")
crush = input("What is the name of your crush? ")
name = name.lower()
crush = crush.lower()
love_string = name + crush
tens = love_string.count('t') +  love_string.count('r') + love_string.count('u') + love_string.count('e')
unit = love_string.count('l') + love_string.count('o') + love_string.count('v') + love_string.count('e') 
val = tens*10 + unit
interpretation  = ''
if val<10 or val>90:
    interpretation = "go together like a coke and mentos"
if val>40 and val<50:
    interpretation = "are alright together"
else: 
    interpretation = 'non'
if interpretation == 'non':
    print(f"Your score is {val}.")
else:
    print(f"Your score is {val}, you {interpretation}.")
