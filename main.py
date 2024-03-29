import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game!")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state name?").title()
    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        guessed_states.append(answer_state)

    # if answer_state == "Exit":
    #     missing_states = []
    #     for i in all_states:
    #         if i not in guessed_states:
    #             missing_states.append(i)
    #     missed_data = pandas.DataFrame(missing_states)
    #     missed_data.to_csv("missing_states.csv")
    #     break

    # In list comprehension list way:-
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        missed_data = pandas.DataFrame(missing_states)
        missed_data.to_csv("missing_states.csv")
        break

screen.exitonclick()
