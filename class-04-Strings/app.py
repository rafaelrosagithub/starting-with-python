my_string = "any text"
print(type(my_string))
print(my_string)
print(f"Concat {my_string} on string.")

print(my_string.upper())
print(my_string.lower())
print(my_string.capitalize())
print(my_string.isupper())
print(my_string.islower())
print(my_string.strip()) # equal to trim
print(my_string.replace("any", "my"))
print(my_string.replace("t", "n", 1))
print(my_string.replace("t", "n"))
print(len(my_string))
print(my_string[2])
print(my_string[2:5])
print(my_string[-7:-6])
print(my_string.index("t"))
print(my_string.index("tex"))

x = "text" in my_string
print(x)
x = "ra" in my_string
print(x)

my_string = """line1,
line2,
line3.
"""
print(my_string)

my_string = "line1,\nline2,\nline3."
print(my_string)

my_string = "line1,\'line2\",\nline3."
print(my_string)


