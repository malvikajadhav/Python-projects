print("Welcome to Treasure Island.")
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')
print("Your mission is to find the treasure.\n") 
choice1 = input("You\'re at a cross road. Where would you like to turn? Type 'Left' or 'Right' ")
choice1 = choice1.lower()
if choice1 == 'left':
    choice2 = input(" You have walked upto a lake. You see an island in the middle of the lake. Type 'wait' if you want to wait for a boat or type 'swim' to swim to the island.")
    choice2 = choice2.lower()
    if choice2 == 'wait':
        choice3 = input(" You arrived at the island unharmed. There is a house with three doors. One 'RED', one 'BLUE' and one 'YELLOW'. Which color do you choose? ").lower()
        if choice3 == 'red':
            print("AAH!! You got burnt by fire.")
            print("GAME OVER") 
        elif choice3 == 'yellow':
            print("OMG YAYYY!!! YOU WIN!!")
        else:
            print("You were attacked by a monster!")
            print("GAME OVER")
            
    else:
        print("Oh no! You were attacked by the trout in the lake!")
        print("GAME OVER") 
else:
    print("Oops you fell into a hole!")
    print("GAME OVER")
