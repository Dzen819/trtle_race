from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

one_more = True

while one_more:
    turtles = []
    is_race_on = False

    for i in range(len(colors)):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[i])
        new_turtle.up()
        new_turtle.goto(x=-230, y=(new_turtle.ycor() - 125) + i * 50)
        turtles.append(new_turtle)

    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

    if user_bet:
        is_race_on = True

    while is_race_on:
        for turtle in turtles:
            if turtle.xcor() > 230:
                win_color = turtle.pencolor()
                is_race_on = False
                if win_color == user_bet:
                    more = screen.textinput(title="You've won!:)", prompt=f"The {win_color} turtle is thw winner!"
                                                                          f" Play again? y/n: ")

                else:
                    more = screen.textinput(title="You've lost!:(", prompt=f"The {win_color} turtle is thw winner! "
                                                                           f" Play again? y/n: ")
                if more == "y":
                    one_more = True
                    screen.clear()
                else:
                    one_more = False
                    screen.clear()
                    screen.bye()
            rand_distance = random.randint(1, 10)
            turtle.forward(rand_distance)

screen.exitonclick()
