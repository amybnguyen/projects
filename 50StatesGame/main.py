import pandas
import turtle
from pen import Pen

screen = turtle.Screen()
screen.title = "US States Game"
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
pen = Pen()

data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()
guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(f"{len(guessed_states)}/50 Guessed States", "What's another state name?")
    answer_state = answer_state.title()

    if answer_state == "Exit":
        missed_states = [state for state in states_list if state not in guessed_states]
        df = pandas.DataFrame(missed_states)
        df.to_csv("states_to_learn.csv")
        break

    if answer_state in states_list and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        print(state_data.x)
        pen.display_state(answer_state, int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
    else:
        print("Not in data")

if len(guessed_states) == 50:
    pen.win()


screen.exitonclick()
