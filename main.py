import turtle
import time
import random
import sys
from tkinter import *

delay = 0.1
score = 0

win = turtle.Screen()
win.title("Snake Game by S.M.H Naghavi")
win.bgcolor("green")
win.setup(width=600, height=600)
win.tracer(0)

# Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "stop"


# Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

# Segments
segments = []

# Score Text
scoreText = turtle.Turtle()
scoreText.hideturtle()
scoreText.penup()
scoreText.goto(-290, 270)
scoreText.pendown()
scoreText.write("Score: {}".format(score), font=("Calibri", "20"))

# Move Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"



# Function to Move the Snake
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)

def exit():
    win.bye()

def restartGame():
    win.bgcolor("green")
    head.showturtle()
    food.showturtle()
    text.clear()
    restart_btn.destroy()
    exit_btn.destroy()
    score = 0
    scoreText.clear()
    scoreText.write("Score: {}".format(score), font=("Calibri", "20"))

# Make Game Over Screen
def gameOver():
    global text, restart_btn, exit_btne
    win.bgcolor("red")
    text = turtle.Turtle()
    text.hideturtle()
    text.penup()
    text.goto(-130,0)
    food.hideturtle()
    text.write("Game Over!", font=("Calibri", "40"))
    head.hideturtle()
    canvas = win.getcanvas()
    restart_btn = Button(canvas.master, text="Restart", bg="green", fg="yellowgreen", command=restartGame)
    restart_btn.place(x=200, y=320)
    exit_btn = Button(canvas.master, text="Exit", bg="navy", fg="skyblue", command=exit)
    exit_btn.place(x=350, y=320)



# bindings
win.listen()
win.onkeypress(go_up, "Up")
win.onkeypress(go_right, "Right")
win.onkeypress(go_left, "Left")
win.onkeypress(go_down, "Down")


# Main game loop
while True:
    win.update()

    # if colision happens between border and the snake
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        #  Hide the segments
        for segment in segments:
            segment.goto(1000,1000)

        # Clear the segments
        segments.clear()
        score = 0
        gameOver()
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)


    # check if any colision happend between the food and the snake
    if head.distance(food) < 20:
        # Move the food to a random location
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)


        # add segments to snake

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("black")
        new_segment.penup()
        segments.append(new_segment)
        score += 10
        scoreText.clear()
        scoreText.write("Score: {}".format(score), font=("Calibri", "20"))

    # Move the end segments first in reverse order
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

    # Move the segment 0 to head
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000,1000)

            # Clear the segments
            segments.clear()
            score = 0
            x = random.randint(-290,290)
            y = random.randint(-290,290)
            food.goto(x,y)


    time.sleep(delay)

win.mainloop()
