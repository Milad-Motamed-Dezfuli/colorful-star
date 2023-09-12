import turtle
a=turtle.Turtle()
a.shape("classic")
a.pencolor("blue")
a.pensize(3)
a.ht()
i=1
l=["blue","red","yellow","green","yellow","purple","blue","orange","red","black","green","blue"]
n=0
while 701>i>0:
    n=n+1
    if n>11:
        n=0
    a.speed(50)
    a.backward(i+20)
    a.right(140)
    a.pencolor(l[n])
    i=i+7
while True:
    a.penup()
    a.pendown()
 
 
