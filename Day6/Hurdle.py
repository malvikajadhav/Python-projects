def turn_right():
    turn_left()
    turn_left()
    turn_left()

def repeat_move():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
for i in range(0,6):
    repeat_move()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
