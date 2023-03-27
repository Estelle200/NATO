import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S State Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
data = pd.DataFrame(data)
states = data.state.to_list()
guessed_states = []
#missing_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        with open("states_to_learn.csv", "w") as states_to_learn:
            missing_states = [state for state in states if state not in guessed_states]
            data = pd.DataFrame(missing_states)

            states_to_learn.write(f"{data}")
        break
    if answer_state in states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        x = int(state_data.x)
        y = int(state_data.y)
        t.goto(x, y)
        t.write(answer_state)





screen.exitonclick()