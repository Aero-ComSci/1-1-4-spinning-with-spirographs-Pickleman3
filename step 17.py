import turtle as trtl

# Create a turtle object
painter = trtl.Turtle()
painter.penup()
painter.goto(-200, 0)
painter.pendown()

# Initial position and movement direction
x = -200
y = 0
move_x = 1
move_y = 1

# Draw the pattern
for _ in range(2):  # Adjust the number of repetitions as needed
    while y < 100:
        x = x + move_x
        y = y + move_y
        painter.goto(x, y)
    move_y = -1
    
    while y > 0:
        x = x + move_x
        y = y + move_y
        painter.goto(x, y)
    move_y = 1

  
 

# Set up the screen to keep it open
wn = trtl.Screen()
wn.mainloop()
