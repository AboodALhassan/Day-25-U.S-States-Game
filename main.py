import turtle
import pandas
screen = turtle.Screen()

screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data["state"]
states_list = states.to_list()

score = 0
guessed_states = []
while len(guessed_states) < 50:
    state_answer = screen.textinput(title=f"{score}/ 50 Guess the State", prompt="What's another State's name: ")
    state_answer = state_answer.title()

    if state_answer == "Exit":
        missing_states = []
        for state in states_list:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_learn.csv")
        break

    if state_answer in states_list:
        t = turtle.Turtle()
        t.hideturtle()
        turtle.penup()
        state_info = data[data.state == f"{state_answer}"]
        turtle.goto(int(state_info.x), int(state_info.y))
        turtle.write(f"{state_answer}")
        score += 1
        guessed_states.append(state_answer)









