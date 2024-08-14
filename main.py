import random
import turtle

t = turtle.Turtle()
t.hideturtle()
text = turtle.Turtle()
text.hideturtle()
screen = turtle.Screen()

screen.setup(1.0, 1.0)

def draw():
  t.color("black")
  t.penup()
  t.goto(0, -50)
  t.pendown()
  t.begin_fill()
  t.circle(100)
  t.end_fill()
  t.penup()
  t.goto(-51, 85)
  t.color("blue")
  t.pendown()
  t.begin_fill()
  for i in range(3):
    t.forward(100)
    t.right(120)
  t.end_fill()

answers = ["yes", "no", "maybe", "You figure\nit out", "absolutely\nnot"]
loop = True
draw()

while loop:
  print("Ask a yes or no question: ")
  
  user = input()
  
  choice = random.choice(answers)
  text.penup()
  text.goto(-20, 40)
  text.color("white")
  text.pendown()
  text.write(choice, font=("Verdana", 10, "normal"))
  
  print("Ask another question? type y for yes or n for no")
  again = input()
  if again == "n":
    loop = False
  else:
    text.clear()