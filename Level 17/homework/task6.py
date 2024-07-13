# Write a program using while loop that makes u guess the correct number, if the number is wrong, make the program ask again.

num = int(input("Enter number from 1 to 10: "))

while True:
    my_guess = int(input("My guess: " ))
    if num == my_guess:
        print("Correct")
        break
    else:
        print("try again")