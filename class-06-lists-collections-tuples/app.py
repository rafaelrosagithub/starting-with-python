# Lists
fruits = ["orange", "lemon", "apple", "grape", "watermelon"]
print(fruits)
print(fruits[0])
print(fruits[-1])
print(fruits[2:])
print(fruits[2:4])

fruits[2] = "melon"
print(fruits)

fruits.append("guava")
print(fruits)

fruits.insert(1, "plum")
print(fruits)

fruits.pop()
print(fruits)

fruits.remove("lemon")
print(fruits)

index = fruits.index("grape")
print(index)

print(fruits.count("lemon"))
print(fruits.count("grape"))

fruits.extend(["banana", "avocado"])
print(fruits)

fruits.sort()
print(fruits)

fruits.reverse()
print(fruits)

fruits2 = fruits
print(fruits2)
fruits3 = fruits.copy()
print(fruits3)
fruits.remove("melon")
print(fruits)
print(fruits2)
print(fruits3)


fruits.clear()
print(fruits)

list_numbers = [33, 44, 45, 7, 11]
print(list_numbers)

list_numbers.sort()
print(list_numbers)

list_numbers.reverse()
print(list_numbers)

# Tuples are immutable
numbers2 = (40, 60) 
print(numbers2)