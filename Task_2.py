import turtle

def draw_koch_segment(t, length, level):
   
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        draw_koch_segment(t, level - 1, length)
        t.left(60)
        draw_koch_segment(t, level- 1, length)
        t.right(120)
        draw_koch_segment(t, level - 1, length)
        t.left(60)
        draw_koch_segment(t, level - 1, length)

def draw_koch_snowflake(t, length, level):
    for _ in range(3):
        draw_koch_segment(t, length, level)
        t.right(120)

def main():
    
    # Set up the turtle
    t = turtle.Turtle()
    t.speed(0)  # Fastest drawing speed
    t.penup()
    t.goto(-150, 90)  # Start position
    t.pendown()
    
    # Get the recursion level from the user
    level=int(input("Enter the level of recursion (e.g.,0,1,2,...):"))

    # Length of each side of the snowflake
    length = 300
    
    draw_koch_snowflake(t, length,level)
    
    # Finish
    turtle.done()

if __name__ == "__main__":
    main()
