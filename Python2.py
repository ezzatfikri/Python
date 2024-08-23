# Define a function called greet_user that:
# Takes one argument, name.
# Prints a greeting message that includes the name.
def greet_user(first_name, last_name,):
    print(f"Hi {first_name} {last_name}!")
greet_user("Isma", "Hanif")

print("----------------------------------------------------------------------")

# Modify the greet_user function:
# Add a second optional argument, greeting, with a default value of "Hello".
# The function should print the greeting followed by the name.
def greet_user(first_name, last_name, greeting="Hello"):
    print(f"{greeting} {first_name} {last_name}!")
greet_user("Isma", "Hanif")

print("----------------------------------------------------------------------")

# Create a function sum_numbers that:
# Takes two arguments, a and b.
# Returns the sum of a and b.
def sum_numbers(a,b):
    print (f" Total number of {b} + {a} = {a+b}")
sum_numbers(3,5)


print("----------------------------------------------------------------------")

# Work with the following list: fruits = ["apple", "banana", "cherry", "date"].
# Perform the following operations:
# Add "elderberry" to the end of the list.
# Remove "banana" from the list.
# Insert "blueberry" at the second position in the list.
# Sort the list in alphabetical order.
fruits = ["apple", "banana", "cherry", "date"]
fruits.append("elderberry")
print(fruits)
fruits.remove("banana")
print(fruits)
fruits.insert(1,"blueberry")
print(fruits)
fruits.sort()
print(fruits)

print("----------------------------------------------------------------------")

# Write a loop that:
# Prints numbers from 1 to 10.
# Stops the loop if the number is 7 (use the break statement).
for i in range(1, 11):
    print(i)
    if i == 7:
        print("Loop Stopped")
        break

print("----------------------------------------------------------------------")

# Write a loop that:
# Prints numbers from 1 to 10.
# Skips the numbers that are multiples of 3 (use the continue statement).
for j in range(1, 11):
    if j % 3 == 0:
        continue
    print(j)