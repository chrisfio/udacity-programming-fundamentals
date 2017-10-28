import turtle

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("red")

    emma = turtle.Turtle()
    emma.shape("triangle")
    emma.speed(1)
    emma.color("blue")

    for i in range (0, 72):
        draw_square(emma)
        emma.right(5)

    #randy = turtle.Turtle()
    #randy.shape("square")
    #randy.circle(100)
    #randy.color("black")

    #acer = turtle.Turtle()
    #acer.shape("square")
    #acer.color("white")

    #for y in range (0,3):
        #acer.left(120)
        #acer.forward(200)

    window.exitonclick()
def draw_square(x_turtle):
    for x in range (0,4):
        x_turtle.forward(200)
        x_turtle.right(90)        

draw_shapes()
    
