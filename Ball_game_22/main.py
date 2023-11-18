from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
screen = Screen()
screen.bgcolor("black")
screen.setup(width=888, height=688)  #setup the screen size
screen.title("pong")
screen.tracer(0) #trace method manage the screen


r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
scoreboard=Scoreboard()


    

screen.listen() #tell screen to listen
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

#to place the paddle right side of the screen
game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed) #speedup th boll after each collision
    screen.update()#this method refresh the screen whenever you start the game 
    ball.move()
    
    #Detact the collision of the ball with wall
    if ball.ycor()> 300 or ball.ycor()< -300:
    #need to bounce
        ball.bounce_y()
        
    #collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) <40 and ball.xcor() < -320:
        ball.bounce_x()
    
    #detect R paddle miss
    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.l_point()
        
    #detect L paddle miss
    if ball.xcor()< -380:
         ball.reset_position()
         scoreboard.r_point()
screen.exitonclick()

