import turtle
import math
import random
import time
import os

choice = 2
level = 1
speed = 4
agility = 5
score = 0

turtle.setup(2610, 1440, 0, 0)

screen = turtle.Screen() 
screen.title("Game")
screen.bgcolor("black")

delay = turtle.Turtle()
delay.color("pink")
delay.hideturtle()
delay.up()
delay.speed(0)
delay.lt(90)

player = turtle.Turtle()

player.color("red")  
player.pensize(100)
player.shapesize(4)
player.shape("turtle")
player.up()
player.speed(0)
player.setheading(90)
player.speed(0)

speed = turtle.Turtle()
speed.shapesize(3)
speed.color("yellow")
speed.shape("square")
speed.speed(0)
speed.up()
speed.hideturtle()

speed2 = turtle.Turtle()
speed2.shapesize(3)
speed2.color("blue")
speed2.shape("circle")
speed2.speed(0)
speed2.up()
speed2.hideturtle()

speed.setposition(1100, 300)
speed.speed(0)

speed2.setposition(1100, 300)
speed2.speed(0)

enemy = turtle.Turtle()
enemy.speed(0)
enemy.color("white")
enemy.shape("turtle")
enemy.up()
enemy.goto(-1000, 0)
enemy.speed(0)
enemy.shapesize(2)
enemy.up()

turtle.hideturtle()
turtle.lt(90)
turtle.fd(500)
turtle.clear()
turtle.color('yellow')
style = ('Arial', 50, 'bold')
turtle.write('Score\n' + " 000" + str(score), font=style, align='center') 

turtle2 = turtle.Turtle()
turtle2.hideturtle()

bullet = turtle.Turtle()
    
bullet2 = turtle.Turtle()


def foward():
    player.fd(speed.ycor() / 25)

def back():
    player.bk(speed.ycor() / 25)

def left():
    player.lt(5)

def right():
    player.rt(5)

def increase():
    speed.sety(speed.ycor() + 5)
    speed2.sety(speed2.ycor() + 5)

def decrease():
    speed.sety(speed.ycor() - 5)
    speed2.sety(speed2.ycor() - 5)

def stop():
    speed.sety(0)

def backto():
    speed.sety(speed2.ycor())

def shoot():
    if delay.ycor() == 0:
        delay.fd(10)
        os.system("afplay laser.wav&")
        bullet2.hideturtle()
        bullet2.pensize(40)
        bullet2.speed(0)
        bullet2.color("green")
        bullet2.up()
        bullet2.goto(player.position())
        bullet2.setheading(player.heading())
        #bullet.showturtle()
        bullet2.speed(0)
        bullet2.down()
        bullet2.fd(hypo)
        bullet2.clear()
        return bullet2

def shootplayer(distance):
    os.system("afplay laser.wav&")
    bullet.up()
    bullet.pensize(50)
    bullet.hideturtle()
    bullet.shapesize(3)
    bullet.speed(0)
    bullet.color("blue")
    bullet.goto(enemy.position())
    bullet.setheading(enemy.heading())
    #bullet.showturtle()
    bullet.speed(0)
    bullet.down()
    bullet.fd(distance)
    bullet.clear()
    return bullet

#screen.onkey(foward, "Up")
#screen.onkey(back, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.onkey(increase, "Up")
screen.onkey(decrease, "Down")
screen.onkey(stop, ".")
screen.onkey(backto, "0")
screen.onkey(shoot, "space")
screen.listen()

while True:
    px = player.xcor()
    py = player.ycor()
    ex = enemy.xcor()
    ey = enemy.ycor()
    adj = (px - ex)
    opp = (py - ey)
    hypo = math.sqrt((adj * adj) + (opp * opp))
    angle = math.degrees(math.acos(adj/hypo))
    if adj < 0:
        angle = 360 - angle
    if adj > 0 and opp < 0:
        angle = 360 - angle
    if adj < 0 and opp > 0:
        angle = 360 - angle
    #print(angle)
    enemy.setheading(angle)
    player.fd(speed.ycor() / 25)
    randomnumber = random.randint(0, 100)
    if randomnumber == 5:
        shootplayer(hypo)
        if abs(bullet.xcor() - player.xcor()) < 7000/hypo and abs(bullet.ycor() - player.ycor()) < 7000/hypo:
            os.system("afplay explosion.wav&")
            player.color("blue")
            player.speed(4)
            shapesize = 4
            while shapesize > 0.1:
                shapesize = shapesize - 0.1
                player.lt(10)
                player.shapesize(shapesize)
            player.hideturtle()
            enemy.hideturtle()
            speed.hideturtle()
            turtle2.color('blue')
            style = ('Arial', 200, 'bold')
            turtle2.write('GAME OVER', font=style, align='center')
            turtle2.hideturtle()
            file1 = open(r"Highscore.txt","r")
            print(file1.read())
            file1.close()
            time.sleep(0.5)
            
            turtle.bye()

    if abs(bullet2.xcor() - enemy.xcor()) < 15 and abs(bullet2.ycor() - enemy.ycor()) < 15:
        os.system("afplay explosion.wav&")
        enemy.color("green")
        enemy.speed(4)
        shapesize = 2
        while shapesize > 0.1:
            shapesize = shapesize - 0.05
            enemy.lt(10)
            enemy.shapesize(shapesize)
        enemy.hideturtle()
        #player.hideturtle()
        speed.hideturtle()
        #turtle.color('green')
        #style = ('Arial', 200, 'bold')
        #level = level + 1
        #turtle.write('Level ' + str(level), font=style, align='center')
        #turtle.hideturtle()
        time.sleep(0.5)
        enemy.speed(0)
        enemy.color("white")
        enemy.shape("turtle")
        enemy.up()
        enemy.goto(random.randint(-1000, 1000), random.randint(-800, 800))
        enemy.speed(4)
        enemy.shapesize(2)
        enemy.showturtle()

        #player.goto(0, 0)
        #player.color("red")  
        #player.pensize(100)
        #player.shapesize(4)
        #player.setheading(90)
        #player.showturtle()
        #turtle.clear()
        bullet.reset()
        bullet2.reset()

        choice = choice + 1

        score = score + 5

        turtle.clear()
        style = ('Arial', 50, 'bold')
        turtle.write('Score\n ' + ("0" * (4 - len(str(score)))) + str(score), font=style, align='center')

    if delay.ycor() != 0:
        delay.sety(delay.ycor() - 1)

    if abs(player.ycor()) >= 720:
        player.setheading(360 - player.heading())

    if abs(player.xcor()) >= 1305:
        player.setheading(player.heading() - 90)
        
    enemy.fd(choice)
        
    

    

    
    
    
