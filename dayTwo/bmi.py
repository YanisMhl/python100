height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight/pow(height, 2))

print("Your bmi = " + str(bmi))