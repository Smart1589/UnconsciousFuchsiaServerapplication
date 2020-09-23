import turtle
t = turtle.Turtle()
t.speed(5)
canvas = t.getscreen()
canvas.bgcolor('gray')
def move(x,y):
  t.penup()
  t.goto(x,y)
  t.pendown() #end of move function
mycolors = {'red', 'orange','peachpuff', 'violet', 'white', 'blue', 'yellow'}
move (0,0)
def flower(length, x, y):
  
  for c in mycolors:
   t.pencolor(c)
   for i in range(4):
    t.rt(90)
    t.forward(length) #end of square loop
   t.penup()
   t.rt(60)
   t.pendown() #color loop ends
move(0,-100)
flower(10)
move(0,0)
flower(10)
move (-20,20)
flower(10)
flower(20, -100,100)
flower(20,-100,40)
flower(20,-100,-20)
x= -20
y= 120
for i in range(5):
  flower(20,x,y)
  x = x + 60
  y = y -60