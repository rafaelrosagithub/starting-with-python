# Comment here

"""
this is also a comment
comment
comment
"""

name = input("Type your name: ")
age = int(input(f"How old are you {name}? "))

birth = 2023 - age

print(name)
print(age)
print(f"His name is {name} and his age is {age}.")
print(f"{name} you were born in {birth}")

# Basic Calculator

num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
result = num1 + num2
print(f"The result is {result}")