import pandas as pd
import turtle
from turtle import Turtle
from scoreboard import Scoreboard

screen = turtle.Screen()
screen.setup(width=800, height=600)
scoreboard = Scoreboard()
screen.title("U.S. States Game")
image = "blank_states_img.gif"


screen.addshape(image)
turtle.shape(image)

df = pd.read_csv("50_states.csv")
print(df['state'].count())

states_list = []
missing_states_list = []

count = 0
while count < 50:
    screen.update()
    answer_state = screen.textinput(title="Guess the state", prompt="What`s another state`s name?").title()

    # If user type "exit" new csv will generate containing all the states that the uses did not guess
    if answer_state == "Exit":
        all_states = df.state.to_list()
        missing_states_list = list(set(all_states).difference(states_list))
        pd.DataFrame(missing_states_list).to_csv("states_to_learn.csv")
        break

    if answer_state in df['state'].values:
        states_list.append(answer_state)
        if states_list.count(answer_state) > 1:
            a = 1
        else:
            cor_x = int(df.loc[df['state'] == answer_state, 'x'])
            cor_y = int(df.loc[df['state'] == answer_state, 'y'])
            state_name = Turtle()
            state_name.hideturtle()
            state_name.penup()
            state_name.goto(cor_x, cor_y)
            state_name.write(f"{answer_state}")
            scoreboard.increase_score()
            count += 1


# Find coordinates in the screen by clicking
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()




