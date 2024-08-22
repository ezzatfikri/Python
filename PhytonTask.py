#Task 1
number = int(input("Enter a number: "))

if number % 2 == 0:
    print (f"The number {number} is even")
else:
    print (f"The number {number} is odd")

#Task 2
num1 = int(input("Enter a number: "))
i = 0

while True:
    i += 1
    print(f"{num1} x {i} = {num1 * i}")

    if i == 12:
        break


#Task 3
firnum = int(input("Enter 1st number: "))
secnum = int(input("Enter 2nd number: "))
thinum = int(input("Enter 3rd number: "))

if firnum > secnum and firnum > thinum:
    print(f"{firnum} is the largest number")
elif secnum > firnum and secnum > thinum:
    print(f"{secnum} is the largest number")
else:
    print(f"{thinum} is the largest number")

#Task 4
word = input("Enter a word: ")
vowels = 'aeiou'
count = 0
for char in word.lower():
    if char in vowels:
        count += 1
print(f"Number of vowels in {word} is {count}")
