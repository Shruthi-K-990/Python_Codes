import time
import datetime as dt
import turtle

t = turtle.Turtle() # create turtle to display time
t1 = turtle.Turtle() # create rect box
s=turtle.Screen()
s.bgcolor("lightblue")
sec= dt.datetime.now().second
min= dt.datetime.now().minute
hr= dt.datetime.now().hour

t1.pensize(4)
t1.color('black')
t1.penup() #no drawing while moving
t1.goto(-20,10)
t1.pendown()  #drawing while moving

#rect box
for i in range(2):
    t1.forward(250)
    t1.left(90)
    t1.forward(100)
    t1.left(90)

t1.hideturtle() #hiding turtle will speed up drawing

while True:
    t.hideturtle()
    t.clear()
    t.write(str(hr).zfill(2)+":"+str(min).zfill(2)
             +":"+str(sec).zfill(2),font=("Calibre",40,"bold")
            )
    time.sleep(1)
    sec+=1

    if sec==60:
        sec=0
        min+=1

    if min==60:
        min=0
        hr+=1

    if hr == 13:
        hr=1