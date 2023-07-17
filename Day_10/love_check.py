# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
# 1. Concat names and convert into lower case
names = name1 + name2

names = names.lower()

# 2. Count occurence of letters in names
t = names.count('t')
r = names.count('r')
u = names.count('u')
e = names.count('e')

true = t + r + u + e
# print(f'T occurs: {t} times \n R occurs: {r} times \n U occurs {u} times \n E occurs {e} times ')

l = names.count('l')
o = names.count('o')
v = names.count('v')
e = names.count('e')

love = l + o + v + e

# print(f'L occurs: {l} times \n O occurs: {o} times \n V occurs {v} times \n E occurs {e} times ')


total_score = str(true) + str(love)
total_score = int(total_score)
# print(total_score)
if total_score < 10 or total_score > 90:
    print(f'Your score is {total_score}, you go together like coke and mentos.')
elif total_score > 40 and total_score < 50:
    print(f'Your score is {total_score}, you are alright together.')
else:
    print(f'Your score is {total_score}')
    
