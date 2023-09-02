# Manipulating Files

# open("path", "mode")
# Mode
# r  - reading
# a  - append / increment
# w  - writing, overwrite if there is anything inside the file
# x  - create file
# r+ - reading + writing

file = open("class-12-Manipulating-files/test.txt", "r")

print(file.readable())
print(file.read())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())

list = file.readlines()
print(list)
print(list[2])

file = open("class-12-Manipulating-files/test2.txt", "w")
file = open("class-12-Manipulating-files/test3.txt", "x")

file.write("Test...\n")
file.write("C\n")
file.write("Kubernetes\n")
file.write("Docker\n")

file.close()

import os

if os.path.exists("class-12-Manipulating-files/test3.txt"):
    # The file need to be closed before it can be removed
    os.remove("class-12-Manipulating-files/test3.txt") # Remove file
else:
    print("File doesn't exist")

os.rmdir("class-12-Manipulating-files/new-folder") # Remove folder
