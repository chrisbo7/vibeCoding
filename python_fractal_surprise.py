import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Fractal Tree Surprise!")
screen.setup(width=900, height=700)

# Set up the turtle
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.width(2)
t.color("#39FF14")
t.penup()
t.goto(0, -250)
t.pendown()

def draw_fractal_tree(t, branch_length, angle, depth):
    if depth == 0 or branch_length < 5:
        t.color(random.choice(["#39FF14", "#00FFFF", "#FF00FF", "#FFD700", "#FF4500"]))
        t.dot(random.randint(6, 14))
        t.color("#39FF14")
        return
    t.forward(branch_length)
    t.left(angle)
    draw_fractal_tree(t, branch_length - random.randint(10, 18), angle + random.randint(-5, 5), depth - 1)
    t.right(angle * 2)
    draw_fractal_tree(t, branch_length - random.randint(10, 18), angle + random.randint(-5, 5), depth - 1)
    t.left(angle)
    t.backward(branch_length)

t.left(90)
draw_fractal_tree(t, 120, 28, 8)

# Add a little surprise message at the end
t.penup()
t.goto(0, -320)
t.color("#FFD700")
t.write("Python is Awesome!", align="center", font=("Arial", 24, "bold"))

screen.mainloop()
