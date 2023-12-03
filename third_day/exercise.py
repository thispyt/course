print("welcome to the Body Mass Index")
weight=float(input("Please write your weight :\n"))
height=float(input("Please write your height :\n"))
body_mass_index=round(weight/(height*height))
if body_mass_index <18.5:
    print(f"Your BMI is {body_mass_index} ,you are underweight")
elif body_mass_index <25:
    print(f"Your BMI is {body_mass_index} ,you have a normal weight")
elif body_mass_index<30:
    print(f"Your BMI is {body_mass_index} ,you are overweight")
elif body_mass_index<35:
    print(f"Your BMI is {body_mass_index} ,you are obese")
else:
    print(f"Your BMI is {body_mass_index} ,you are clinically obese")