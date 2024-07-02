age = int(input("enter ur age: "))
total = int(input("enter total price: "))

if age>=60:
    print("discounted") 

if age<60 and total<=100:
    print("discount not available")

if age<60 and total>=100:
    print("discounted")

if age>=60 and total>=100:
    print("2X discount")