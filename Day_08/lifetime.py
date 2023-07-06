# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆
age = int(age)
total_days = 365 * 90
total_weeks = 90 * 52
total_months = 90 * 12

# Convert Age in days, weeks, months
your_days = age * 365
your_weeks = age * 52
your_months = age * 12


left_days = total_days - your_days
left_weeks = total_weeks - your_weeks
left_months = total_months - your_months


print(f"You have {left_days} days, {left_weeks} weeks, and {left_months} months left")
#Write your code below this line 