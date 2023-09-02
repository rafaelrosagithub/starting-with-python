# Loops: While and For
print("Start...")
i = 1

while i < 10:
    print(i)
    i += 1
print(i)

fruits = ["Orange", "Lemon", "Apple"]

for item in fruits:
    print("Item: ", item)

phrase = "Studying Python"

for letter in phrase:
    print(letter)

for index in range(8, 20, 3):
    print(index)

for index in range(len(fruits)):
    print(f"Index: {index}, Name: {fruits[index]}")

for index in range(8):
    if index == 0:
        print(f"First line: {index}")
    else:
        print(f"Other Line: {index}")

matrix_numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for line in matrix_numbers:
    print(line)
    for colunm in line:
        print(colunm)

print("End.")