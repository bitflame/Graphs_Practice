import turtle


def draw_snowflake(turtle, length, depth):
    # recursive termination
    if depth == 0:
        return
    for _ in range(6):
        turtle.right(60)
        turtle.forward(length)

        # recursive descent
        draw_snowflake(turtle, length // 3, depth - 1)
        turtle.back(length)

    screen = turtle.Screen()
    turtle.speed(100)
    draw_snowflake(turtle, 240, 5)
    screen.exitonclick()


draw_snowflake(turtle, 50, 50)
