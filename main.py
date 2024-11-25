import turtle
import pandas

screen = turtle.Screen()
screen.setup(750, 500)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Correct States", prompt="What's another state's name?").title()

    missed_states = []
    if answer_state == "Exit":
        for state in all_states:
            if state not in guessed_states:
                missed_states.append(state)
        missed_states_df = pandas.DataFrame(missed_states)
        missed_states_df.to_csv("states_To_Learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        x_cor = state_data.x.item()
        y_cor = state_data.y.item()
        t.goto(x_cor, y_cor)
        t.write(answer_state)

