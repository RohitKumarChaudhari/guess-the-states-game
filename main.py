import turtle
import pandas as pd


screen = turtle.Screen()
screen.title("U.S State Name Guess")
image = "indian map states outline.gif"
screen.addshape(image)

turtle.shape(image)

state_data = pd.read_csv("28_states_India.csv")
state_name = state_data.state.to_list()
print(state_name)

state = turtle.Turtle()

guessed_state = []
while len(guessed_state) < 28:

    answer_state = screen.textinput(title=f"{len(guessed_state)}/28 State Correct", prompt="guess the next state?").title()

    if  answer_state == "Exit":
        missing_state = []
        for states in state_name:
            if states not in guessed_state:
                missing_state.append(states)
        new_data = pd.DataFrame(missing_state)
        new_data.to_csv("state_to_learn.csv")
        break
    if answer_state in state_name:
        guessed_state.append(answer_state)
        state_cor_x = state_data.x[state_data.state == answer_state].iloc[0]
        state_cor_y = state_data.y[state_data.state == answer_state].iloc[0]
        state.penup()
        state.hideturtle()
        state.goto(state_cor_x, state_cor_y)
        state.write(answer_state)


