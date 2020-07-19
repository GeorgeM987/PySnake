import turtle
import time
import random
#
from decorators import *
#
#
#
delay = 0.1
score = 0
high_score = 0

#screen setup
wn = turtle.Screen()
wn.title('Snake by MGA')
wn.bgcolor(0.2, 0.2, 0.2)
wn.setup(width=600, height=600)
wn.tracer(0)

#snake head
head = turtle.Turtle()
head.speed(0)
head.shape('circle')
head.shapesize(1.5, 1.5)
head.color('black')
head.penup()
head.goto(0, 0)
head.direction = 'stop'

#snake food
food = turtle.Turtle()
food.speed(10)
food.shape('circle')
food.color('red')
food.penup()
food.goto(0, 100)

#more snake food
more_food = turtle.Turtle()
more_food.speed(10)
more_food.shape('circle')
more_food.color('orange')
more_food.hideturtle()
more_food.penup()
more_food.goto(0, 100)

#more snake food
timed_food = turtle.Turtle()
timed_food.speed(10)
timed_food.shape('circle')
timed_food.color('magenta')
timed_food.hideturtle()
timed_food.penup()
timed_food.goto(0, 100)

segments = []

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.hideturtle()
pen.penup()
pen.goto(0, 260)
pen.write('Score: 0 HighScore: 0 Speed: 1', align='center', font=('Courier', 20, 'normal'))
pen.goto(0, 240)
pen.write('Press Q to quit or W, A, S, D to move the snake. Enjoy!', align='center', font=('Courier', 12, 'normal'))
pen.goto(0, 260)

#functions
def go_up():
    head.direction = 'up'

def go_down():
    head.direction = 'down'

def go_left():
    head.direction = 'left'

def go_right():
    head.direction = 'right'

def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)
        
    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)
        
    if head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)
        
    if head.direction == 'right':
        x = head.xcor()
        head.setx(x + 20)

def countdown(t):
    if t > 0:
        t -= 1
    return t

tw = 0.25
tc = 0.25
def game_over(x=tw, y=tc):
    pen.home()
    pen.write('Game Over', align='center', font=('Courier', 28, 'normal'))
    pen.clear()
    time.sleep(x)
    pen.write('', align='center', font=('Courier', 28, 'normal'))
    pen.clear()
    time.sleep(y)

#key bindings
wn.listen()
wn.onkeypress(go_up, 'w')
wn.onkeypress(go_down, 's')
wn.onkeypress(go_left, 'a')
wn.onkeypress(go_right, 'd')
wn.onkeypress(turtle.bye, 'q')

t = 3

#game loop
while True:
    wn.update()

    #check for collision with margin
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        @flashing
        def flashing_go(time_w, time_c):
            game_over(time_w, time_c)
        flashing_go(tw, tc)
        pen.goto(0, 260)
        head.goto(0, 0)
        head.direction = 'stop'

        #hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        #clear the segments list
        segments.clear()

        #reset score
        score = 0

        #reset the delay
        delay = 0.10

        @map_min_max
        def speed(speed_score):
            speed_score = delay
            return speed_score

        #update the score
        more_food.hideturtle()
        timed_food.hideturtle()
        pen.clear()
        pen.write('Score: {} HighScore: {} Speed: {}'.format(score, high_score, speed(delay)), align='center', font=('Courier', 20, 'normal'))

    #check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            @flashing
            def flashing_go(time_w, time_c):
                game_over(time_w, time_c)
            flashing_go(tw, tc)
            pen.goto(0, 260)
            head.goto(0, 0)
            head.direction = 'stop'

            #hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            #clear the segments list
            segments.clear()

            #reset the score
            score = 0

            #reset the delay
            delay = 0.10

            @map_min_max
            def speed(speed_score):
                speed_score = delay
                return speed_score

            #update the score display
            more_food.hideturtle()
            timed_food.hideturtle()
            pen.clear()
            pen.write('Score: {} HighScore: {} Speed: {}'.format(score, high_score, speed(delay)), align='center', font=('Courier', 20, 'normal'))
        
    #check for collision with the food
    if head.distance(food) < 20:
        #move the food to a random spot
        x = random.randrange(-280, 280, 20)
        y = random.randrange(-280, 280, 20)
        food.goto(x, y)

        #add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('circle')
        new_segment.color('green')
        new_segment.penup()
        segments.append(new_segment)

        @decrement_delay
        def reduce_delay(time):
            return time

        delay = reduce_delay(delay)

        @map_min_max
        def speed(speed_score):
            speed_score = delay
            return speed_score

        @increment_score
        def increase_score(result):
            return result

        score = increase_score(score)

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write('Score: {} HighScore: {} Speed: {}'.format(score, high_score, speed(delay)), align='center', font=('Courier', 20, 'normal'))
        
    
    #double the food/reward
    if score >= 50:        
        more_food.showturtle()
        if head.distance(more_food) < 20:
            x = random.randrange(-280, 280, 20)
            y = random.randrange(-280, 280, 20)
            more_food.goto(x, y)

            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape('circle')
            new_segment.color('green')
            new_segment.penup()        
            segments.append(new_segment)

            @decrement_delay
            def reduce_delay(time):
                return time

            delay = reduce_delay(delay)

            @map_min_max
            def speed(speed_score):
                speed_score = delay
                return speed_score

            @increment_score
            def increase_score(result):
                return result

            score = increase_score(score)

            if score > high_score:
                high_score = score

            pen.clear()
            pen.write('Score: {} HighScore: {} Speed: {}'.format(score, high_score, speed(delay)), align='center', font=('Courier', 20, 'normal'))

    #triple the food/reward + time
    if score >= 150:
        timed_food.showturtle()
        if head.distance(timed_food) < 20:
            x = random.randrange(-280, 280, 20)
            y = random.randrange(-280, 280, 20)
            timed_food.goto(x, y)

            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape('circle')
            new_segment.color('green')
            new_segment.penup()        
            segments.append(new_segment)

            @decrement_delay
            def reduce_delay(time):
                return time

            delay = reduce_delay(delay)

            @map_min_max
            def speed(speed_score):
                speed_score = delay
                return speed_score

            @increment_score
            def increase_score(result):
                return result

            score = increase_score(score)

            if score > high_score:
                high_score = score

            pen.clear()
            pen.write('Score: {} HighScore: {} Speed: {}'.format(score, high_score, speed(delay)), align='center', font=('Courier', 20, 'normal'))
            if t <= 3:
                countdown(t)
                print(countdown(t))
            if t < 1:
                x = random.randrange(-280, 280, 20)
                y = random.randrange(-280, 280, 20)
                timed_food.goto(x, y)
            
    #move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    #move segment 0 where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    
    move()

    time.sleep(delay)

wn.mainloop()
                        
