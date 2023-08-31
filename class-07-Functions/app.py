def my_function(name):
    print("my_function()")
    print(f"Name: {name}")

def function2(number1, number2):
    print(f"Number1: {number1}, Number2: {number2}")

def function3(name, number1, number2):
    my_function(name)
    function2(number1, number2)

def sum(num1, num2):
    return num1 + num2

def higher_number(list_numbers):
    list_numbers.sort()
    list_numbers.reverse()
    return list_numbers[0]

print("Start")

my_function("Rafael")
function2(3, 5)
function3("John", 5, 7)
total = sum(25, 30)
print(f"Total: {total}")

result = higher_number([345, 987, 34, -3656, 56, 2345])
print(result)

print("End")