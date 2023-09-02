# Exception handling, Try-Except-Finally

try:
    number = int(input("Enter a number: "))
    print(number)
    10/0
except ZeroDivisionError:
    print("Division by zero is not possible")
except ValueError:
    print("Enter a valid value")
except:
    print("Unexpected error..")
finally:
    print("Finally is always executed")

