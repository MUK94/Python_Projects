#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")
total_bill = int(input("What was the total bill?: $"))
percentage1 = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
percentage2 = (total_bill * percentage1) / 100
total_people = int(input("How many people to split the bill? "))
pay_per_person = round((total_bill + percentage2) / total_people , 2)
# print(total_bill, percentage)
print(f"Each person shoud pay: ${pay_per_person}")