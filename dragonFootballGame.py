# Dragon clicker
import turtle

# Creating the screen, setting the title and background color
main_window = turtle.Screen()
main_window.title("Dragon game")
main_window.bgcolor("green")

# Register the gif shape
main_window.register_shape("sasukevDragonGIF.gif")

# Adding speed to the dragon shape
sasukev = turtle.Turtle()
sasukev.shape("sasukevDragonGIF.gif")
sasukev.speed(1)







main_window.mainloop()

