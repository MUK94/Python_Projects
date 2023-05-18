# 1. Using Recursion
def reverse_str(my_string):
    my_string = str(my_string)
    if len(my_string) <= 1:
        return my_string

    else:
        return reverse_str(my_string[1:]) + my_string[0]

print(reverse_str("Mouctar"))

# 2. Using slice operator
my_string = "Mouctar"
reversed_string = my_string[::-1]
print(reversed_string)

