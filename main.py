import turtle
t = turtle.Turtle()
t.speed(100)
canvas = t.getscreen()
canvas.bgcolor('gray')
mycolors = ['red','orange','green','peachpuff','violet','white','blue','yellow']
def flower(length,x,y):
  t.penup()
  t.goto(x,y)
  t.pendown()
  for c in mycolors:
    t.pencolor(c)
    for i in range(4):
      t.rt(90)
      t.forward(length) #end of square loop
    t.penup()
    t.rt(45)
    t.pendown()  #color loop ends
x = -120
y = 120
for i in range(5):
  flower(20,x,y)
  x = x + 60
  y = y - 60