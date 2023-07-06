# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆
person_height = float(height)
person_weight = float(weight)
BMI = (person_weight / (person_height ** 2))
print(round(BMI))