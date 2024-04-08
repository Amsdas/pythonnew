import turtle

def snowflake(t, length_side, levels):
    if levels == 0:
        t.forward(length_side)
        return
    length_side /= 3.0
    snowflake(t, length_side, levels-1)
    t.left(60)
    snowflake(t, length_side, levels-1)
    t.right(120)
    snowflake(t, length_side, levels-1)
    t.left(60)
    snowflake(t, length_side, levels-1)

def main():
    screen = turtle.Screen()
    screen.setup(800, 800)
    screen.bgcolor("skyblue")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-150, 150)
    t.pendown()
    t.color("white")

    length = 300
    levels = 4

    for _ in range(6):
        snowflake(t, length, levels)
        t.right(60)

    screen.mainloop()

if __name__ == "__main__":
    main()
