import pandas as pd
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

df = pd.read_csv("50_states.csv")


while True:
    screen.update()
    answer_state = screen.textinput(title="Guess the state", prompt="What`s another state`s name?").capitalize()
    if answer_state in df['state'].values:
        cor_x = df.loc[df['state'] == answer_state, 'x']
        cor_y = df.loc[df['state'] == answer_state, 'y']
        print(cor_y)
        print(cor_x)


    screen.exitonclick()



