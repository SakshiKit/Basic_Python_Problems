height = float(input("enter you height:"))
weight = int(input("enter you weight:"))

bmi = weight / (height ** height)
bmi_total = weight / (height * height)

if bmi_total < 18.5:
    print("you are underweight")
elif bmi_total < 25:
    print("you have normal weight")
elif bmi_total < 30:
    print("you are slightly overweight")
elif bmi_total < 35:
    print("you are obese")
else:
    print("you are clinically obese")
