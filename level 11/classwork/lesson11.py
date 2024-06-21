# asks the user to enter the savings

savings = float(input("enter your savings: "))

# covert the user input into a float value and update the variable

updsavings = (savings)

# Savings grow after 1 year at a 5% annual intrest rate 

balance = updsavings * 1.10

# convert the balance into a string and update the variable

balance = str(balance)

# concatenate the 2 strings to produce a message

message = "amount in 1 year", + balance

# display the messsage

print(message)