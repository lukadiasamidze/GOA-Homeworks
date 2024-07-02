weight = float(input("Enter your weight:"))

height = float(input("Enter your height: "))

BMI = weight / height* 2

print(BMI)

if BMI<18.5:
    print("Underweight")

if BMI>18.5  and BMI<24.9:
    print("Normalweight")

if BMI>25 and BMI<29.9:
    print("Overweight")

if BMI>=30:
    print("More than overweight")