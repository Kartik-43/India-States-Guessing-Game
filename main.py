import turtle
import pandas


# To Find Coordinates Of the States Of INDIA Using Turtle...
# def a(x, y):
#   print(x,y)
# turtle.onscreenclick(a)
# turtle.mainloop()


screen = turtle.Screen()
screen.title('India States Game')

img = 'India.gif'
screen.addshape(img)
turtle.shape(img)

data = pandas.read_csv('India Coords turtle.csv')
all_states = data.State.to_list()

guessed_state = []

while len(guessed_state) < 38:

    answer_state = screen.textinput(title=f'{len(guessed_state)}/38 States Correct',
                                    prompt="What's another state's name? ").title()
    # If answer is one of the states in all the states...
    # if they got it right
    # Creates a turtle to write the name of the states at the state's coordinates

    if answer_state == 'Exit':
        missing_states = []
        for states in all_states:
            if states not in guessed_state:
                missing_states.append(states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('States to learn.csv')
        break

    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.State == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

screen.exitonclick()
