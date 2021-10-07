#packages
import turtle
import time
import random
score=0
# settings of the screen
wn=turtle.Screen()
wn.title('Snake game made by S.M.H Naghavi')
wn.bgcolor('green')
wn.setup(width=600,height=600)
wn.tracer(0)
#creating the head object
head=turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('white')
head.penup()
head.goto(0,0)
head.direction='stop'

#creating the food object
food=turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(0,100)

#segments
segment=[]
segments=[]


#functions
def go_up():
    head.direction='up'

def go_down():
    head.direction='down'

def go_right():
    head.direction='right'

def go_left():
    head.direction='left'

def move():
    if head.direction=='up':
        y=head.ycor()
        head.sety(y+20)
    
    if head.direction=='down':
        y=head.ycor()
        head.sety(y-20)

    if head.direction=='right':
        x=head.xcor()
        head.setx(x+20)

    if head.direction=='left':
        x=head.xcor()
        head.setx(x-20)
    

#binding
wn.listen()
wn.onkeypress(go_up,'w')
wn.onkeypress(go_down,'s')
wn.onkeypress(go_right,'d')
wn.onkeypress(go_left,'a')

while True:
    wn.update()
    #if colision between the border and snake happend then:
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        wn.title('Game over.')
        head.goto(0,0)
        head.direction='stop'
        time.sleep(1)
        wn.title('Snake game made by Sayed MohammadHadi Naghavi')

        #hide the segments
        for segment in segments:
            segment.goto(1000,1000)

        #clear the segments
        segments.clear()
        score=0

    #if colision between the food and head happend then:
    if head.distance(food)<20:
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)
        #add segments to snake
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('black')
        new_segment.penup()
        segments.append(new_segment)
        score=score+10
        wn.title(score)
        
        
        
        
    #move the segments in reverse order
    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)
    #move the segment 0 to the head
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)
    
        
    move()
    time.sleep(.1)
wn.mainloop()
