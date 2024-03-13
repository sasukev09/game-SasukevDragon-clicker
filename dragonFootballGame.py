# Dragon clicker
import turtle

# Creating the screen, setting the title and background color
main_window = turtle.Screen()
main_window.setup(900, 600)
main_window.title("Dragon game")
main_window.bgcolor("green")

# Register the gif shape
main_window.register_shape("sasukevDragonGIF.gif")

# Adding speed to the dragon shape
sasukev = turtle.Turtle()
sasukev.shape("sasukevDragonGIF.gif")
sasukev.speed(1)

clicks = 0
pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0, 200)
pen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 32, "bold"))


# Function that tracks clicks


def clicked(x,y):
    global clicks
    clicks += 1
    pen.clear()
    pen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 32, "bold"))

sasukev.onclick(clicked)


main_window.mainloop()
