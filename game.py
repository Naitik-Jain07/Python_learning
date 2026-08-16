import turtle
import pandas
screen = turtle.Screen()
screen.title("US State games")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# #to get coordinates but its already there in 50 states.csv
# def get_mouse_click_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop() # better alternative
# # screen.exitonclick() coz game is about clicking only

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title =f"{len(guessed_states)}/50 Guess the state" , prompt = "What is your guess?" ).capitalize()
    print(answer_state)

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
            new_data = pandas.DataFrame(missing_states)
            new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item() , state_data.y.item())
        t.write(state_data.state.item())

# state_data.x means Give me the x column of state_data, while keeping its Pandas index."
#state_data.x.item gives tge actual integer

#states_to_learn.csv
#OWN APPROACH FOR THIS
# with open("states_to_learn.csv", "w") as f:
#     for i in range (len(all_states)):
#         for j in range(len(guessed_states)):
#             if all_states[i] != guessed_states[j]:
#                 f.write(all_states[i])
#                 f.write("\n")

screen.exitonclick()




