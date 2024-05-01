height=float(input("Enter your height in meter : "))
weight=float(input("Enter you weight in kg : "))
bmi = weight/height**2
if bmi<=18.5:
    print(f"Your bmi is {bmi} and you are underweight")
elif bmi<=25:
    print(f"Your bmi is {bmi} and you are normal weight")
elif bmi<=35:
    print(f"Your bmi is {bmi} and you are obese")
else:
    print(f"Your bmi is {bmi} and you are overweight")
