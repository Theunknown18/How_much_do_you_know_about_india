import turtle
FONT = ("Courier", 40, "bold")
SMALLFONT=("Courier", 10, "bold")
import pandas
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()
screen=turtle.Screen()
screen.register_shape("India.gif")
turtle.shape("India.gif")
data=pandas.read_csv('states_and_ut.csv')
list_of_states=[]
list_of_states=data.state.values.tolist()
life=10
cnt=0
guessed_states=[]
while len(guessed_states) <= 36:
    answer_state=screen.textinput(title=f"{cnt}/{len(list_of_states)} States/Ut",prompt="Enter the name of State/Ut ").title()
    if answer_state in list_of_states:
        cnt+=1
        state_data=(data[data.state==answer_state])
        xcor= int(state_data.x.iloc[0])
        ycor=int(state_data.y.iloc[0])
        nw=turtle.Turtle()
        nw.pu()
        nw.hideturtle()
        nw.goto(xcor,ycor)
        nw.write(answer_state)
        guessed_states.append(answer_state)

    if cnt==36:
        turtle.color("Blue")
        turtle.goto(0, 0)
        turtle.write("You Won", align="Center", font=FONT)
    if life==0:
        turtle.color("Blue")
        turtle.goto(0,0)
        turtle.write("Game Over,You Lost",align="Center",font=FONT)
        game_is_on=False
    if answer_state == "Exit":
        missing_states=[]
        for state in list_of_states:
            if state not in guessed_states:
                missing_states.append(state)
            new_data=pandas.DataFrame(missing_states)
            new_data.to_csv("States_you_missed.csv")
        exit(0)
    else:
        life-=1
screen.exitonclick()
