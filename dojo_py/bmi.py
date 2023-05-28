# Just a test create a BMI calculator
# bmi = weight_k / (height_m^2)


weight = float(input("Enter weight in (kg): "))
height = float(input("Enter Height in (m): "))

bmi = weight/(height ** 2)
if bmi <= 25:
    print(f"Your BMI is {bmi}. Your BMI status is FIT")
else:
    print(f"Your BMI is {bmi}. You're kinda overweight")
