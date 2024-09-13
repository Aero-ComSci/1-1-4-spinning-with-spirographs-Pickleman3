import turtle as trtl

# Create a turtle object
painter = trtl.Turtle()
painter.penup()
painter.goto(-200, 0)
painter.pendown()

# Draw the pattern in an infinite loop
while True:
    # Initial position and movement direction for the first pattern
    x = -200
    y = 0
    move_x = 1
    move_y = 1

    # Draw the first pattern
    for _ in range(2):
        while y < 100:
            x += move_x
            y += move_y
            painter.goto(x, y)
        move_y = -1

        while y > 0:
            x += move_x
            y += move_y
            painter.goto(x, y)
        move_y = 1

    # Move back to the starting position for the second pattern without drawing
    painter.penup()
    painter.goto(-200, 0)
    painter.pendown()
    
    # Reset position for the second pattern
    x = -200
    y = 0
    move_y = -1  # Start moving down

    # Draw the second pattern
    for _ in range(2):
        while y > -100:
            x += move_x
            y += move_y
            painter.goto(x, y)
        move_y = -move_y  # Toggle move_y

        while y < 0:
            x += move_x
            y += move_y
            painter.goto(x, y)
        move_y = -move_y  # Toggle move_y

    # Move back to the starting position for the next cycle without drawing
    painter.penup()
    painter.goto(-200, 0)
    painter.pendown()

# Set up the screen to keep it open
wn = trtl.Screen()
wn.mainloop()
