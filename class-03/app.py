# Working with numbers

num1 = 5
num2 = 3.5

print(type(num1))
print(type(num2))

a = float(num1)
print(a)
print(type(a))

b = int(num2)
print(b)
print(type(b))

a = float("5")
b = int(float("3.5"))

print(type(a))

print(num1 + num2) # plus
print(num1 - num2) # minus
print(num1 * num2) # multiplication
print(num1 / num2) # division
print(num1 ** num2) # exponentiation
print(num1 % num2) # mod
print(num1 // num2) # floor division

print(3 + 5 * 7 + 3)
print((3 + 5) * 7 + 3)

print(abs(-15))
print(pow(3, 3))
print(max(1, 5))
print(min(1, 5))
print(round(8.3))
print(round(8.8))

import math
print(math.floor(8.8))
print(math.ceil(8.8))
print(math.sqrt(49))