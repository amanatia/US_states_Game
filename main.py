import turtle
import pandas

screen = turtle.Screen()
screen.title("State Guessing Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
'''
# Get the x,y values of the click on the map 
def get_mouse_click_coor(x, y):
    print(x, y)
turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()
# when we get the values we put them in the csv file 
'''
data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()
states_count = 0



y_list = data["y"].to_list()
x_list = data["x"].to_list()

 
guessed_states = []
while len(guessed_states) < 50:
    
    answer = screen.textinput(title= f"{len(guessed_states)}/50 Guess the State", prompt="What's another state's name?").title()
    
    if answer == "Exit":
        unguessed_states = [state for state in states if state not in guessed_states]
        new_file = pandas.DataFrame(unguessed_states)
        new_file.to_csv("unguessed_states.csv")  
        break
                 
    for state in states:
        if answer == state:
            guessed_states.append(answer)
            
            correct_answer = turtle.Turtle()
            correct_answer.penup()
            correct_answer.hideturtle()
            
           
            
            
            
            state_index = states.index(answer)
            
            y = y_list[state_index]
            x = x_list[state_index]
            
            correct_answer.goto(x, y)    
            correct_answer.write(answer)    
            
            # Alternatively:
            ''' if answer in states:
                    correct_answer = turtle.Turtle()
                    correct_answer.penup()
                    correct_answer.hideturtle()
                    
                    state_data = data[data.state==answer]
                    
                    correct_answer.goto(state_data.x.item(), state_data.y.item())
                    correct_answer.write(answer) or correct_answer.write(state_data.state.Item())
                    '''

