# task 1 = tuples
fruits = ("apple", "banana", "cherry", "date")
print(f"The first fruit is {fruits[0]}")
print(f"The last fruit is {fruits[-1]}")

numbers = (1, 2, 3, 4, 5)
a, b = numbers[:2]
rest = numbers[2:]
print(a, b, rest)

temp = list(fruits)
temp[1] = "blueberry"
fruits = tuple(temp)
print(f"By using temp, i change the tuples to list and i use temp[1] = blueberry to change the second element, so the new list is {fruits}, as you can see the banana already switch to {fruits[1]}")

# task 2 = sets
colors = {"red", "green", "blue", "yellow"}
colors.add("purple")
print(f"the new set is {colors}")

primary_colors = {"red", "blue", "yellow"}

intersection_set = colors & primary_colors
print(f"the intersection set is {intersection_set}")

union_set = colors | primary_colors
print(f"the union set is {union_set}")

difference_set = colors - primary_colors
print(f"the difference set is {difference_set}")

print (f"Is there is green color in primary? The answer is {"green" in primary_colors}")
print (f"Is there is orange color not in colors? The answer is {"orange" not in colors}")

# task 3 = dictionaries
student_grades = {"Alice": 85, "Bob": 90, "Charlie": 78, "Diana": 92}
print(f"This is bob's grade {student_grades['Bob']}")

student_grades.update({"Eve": 88})
print(f"The new dictionary after add Eve is {student_grades}")

student_grades.update({"Alice": 95})
print(f"The new dictionary after update Alice grade is {student_grades}")

student_grades.pop("Charlie")
print(f"The new dictionary after remove Charlie is {student_grades}")

for student, grade in student_grades.items():
    print(f"Student: {student}, Grade: {grade}")

