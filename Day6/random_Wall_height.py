def turn_right():
    turn_left()
    turn_left()
    turn_left()

def repeat_move():
    turn_left()
    move()
    while right_is_clear()!= True:
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear()== True:
        move()
    turn_left()    
    
while at_goal()!=True:
    if wall_in_front() == True:
        repeat_move()
    else:
        move()
