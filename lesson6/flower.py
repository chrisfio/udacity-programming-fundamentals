import turtle

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("white")

    flower = turtle.Turtle()
    flower.shape("triangle")
    flower.speed(100)
    flower.color("green")
    flower.left(10)
    
    for i in range (0, 72):
        draw_arrow(flower)
        flower.left(5)

    flower.right(100) 
    flower.forward(350)
    
    window.exitonclick()
def draw_arrow(x_turtle):
    x_turtle.forward(100)
    x_turtle.right(45)
    x_turtle.forward(100)
    x_turtle.right(135)
    x_turtle.forward(100)
    x_turtle.right(45)
    x_turtle.forward(100)
    x_turtle.right(135)

draw_shapes()
    
