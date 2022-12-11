from turtle import Turtle, Screen
import random


#initialize global variables
SCREEN = Screen()
#make sure screen setup is prior to USER_BET to avoid conflicting screen dimension issue
SCREEN.setup(width=500, height=400)
ALL_TURTLES = []
Y_AXIS = [-150, -90, -30, 30, 90, 150]
COLORS = ['red', 'blue', 'yellow', 'orange', 'green', 'purple']
USER_BET = SCREEN.textinput(title='Who will win the race?', prompt='Your Choices are (red/blue/yellow/orange/green/purple)')


#create the race turtles
for i in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(COLORS[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=Y_AXIS[i])
    ALL_TURTLES.append(new_turtle)


#when user bets activate race
if USER_BET:
    race = True


#start race and end once xcor reaches x distance
try:
    while race:
        for i in ALL_TURTLES:
            if i.xcor() > 230:
                race = False
                winning_color = i.pencolor()
                if winning_color == USER_BET:
                    print(f'You\'ve won! The winning color was {winning_color}!')
                else:
                    print(f'Sorry you lose. The winning color was {winning_color} :(')


        #generate random functionality for turtles
        for i in ALL_TURTLES:
            random_distance = random.randint(0, 10)
            i.forward(random_distance)

except KeyboardInterrupt:
    print('\nSee you later.')

SCREEN.exitonclick()
