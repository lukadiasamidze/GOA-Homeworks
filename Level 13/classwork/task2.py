# take steps and minutes as inputs
steps = int(input(enter your steps: ))
active_minutes = int(input(enter how many minutes you were walking to achieve the fitness goal))

# store the result of the operation in the variable
goal_achieved = (steps > 10000) or (active_minutes > 30)
# display the result on the screen
print(goal_achieved)
