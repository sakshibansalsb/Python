# try - except
#1. Write a program that asks the user for their age. Use a try-except block to handle the case where the user enters a non-numeric value. If an error occurs, display a message asking for a valid number.
try:
    age = int(input("Please enter your age: "))
    print(f"Your age is {age}.")
except ValueError:
    print("Invalid input. Please enter a valid number.")

Output:- Please enter your age: 22
        Your age is 22.

--------------------------------------------------------------------------------------------------------------------------
#2. Write a program that tries to open a file for reading. Use a try-except block to catch potential errors like the file not existing or permission issues. If an error occurs, display a user-friendly message.
try:
    filename = input("Please enter the filename to open: ")
    with open(filename, 'r') as file:
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
except PermissionError:
        print(f"Error: You do not have permission to read the file '{filename}'.")
except Exception as e:
        print(f"An unexpected error occurred: {e}")

OUTPUT:-Please enter the filename to open:desk.py
        Error: The file 'desk.py' does not exist.
--------------------------------------------------------------------------------------------------------------------------

#3.Write a program that calculates the area of a circle.  Use a try-except block to prevent division by zero when the user enters a zero radius. In the except block, display a message explaining the error.
try:
    radius = int(input("Enter the radius of the circle: "))
    if radius < 1:
        raise Exception("Please give a valid radius")
    else:
        area = 3.14 * radius * radius
        print(f"Area of the circle is {area}")
except Exception as e:
    print(f"An error occurred: {e}")

OUTPUT :- 1) Enter the radius of the circle:7
             Area of the circle is 153.86
          2) Enter the radius of the circle:0
             An error occurred: Please give a valid radius
--------------------------------------------------------------------------------------------------------------------------

#4. Create a custom exception class named "ValueOutOfRangeError". Write a program that takes a number as input and checks if it's within a specific range. Use a try-except block to catch the custom exception and display a relevant error message.
try:
    number = int(input("Enter the number between 1 and 100: "))
    if number <1 or number >100:
        raise Exception("Please give a number between 1 aand 100")
    else:
        print(f"Given number is {number}")
except Exception as e:
    print(f"An error occurred: {e}")
OUTPUT:- 1) Enter the number between 1 and 100: 20
            Given number is 20
         2)Enter the number between 1 and 100: 0
            An error occurred: Please give a number between 1 aand 100

--------------------------------------------------------------------------------------------------------------------------

#5. Simulate a scenario where you have a function that performs an operation and might raise an exception.  Write another function that calls the first function and wraps it in a try-except block. In the outer try-except, handle a different type of exception that might occur during the function call. This demonstrates handling exceptions at different levels in your code.

def divide_numbers(a, b):
    """Performs division and might raise a ZeroDivisionError."""
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b

def perform_operation(a, b):
    """Calls divide_numbers and handles any general exceptions that might occur."""
    try:
        result = divide_numbers(a, b)
        print(f"The result of dividing {a} by {b} is {result}")
    except ZeroDivisionError as e:
        print(f"Error in divide_numbers: {e}")
    except Exception as e:
        print(f"An unexpected error occurred in perform_operation: {e}")

# Example usage
try:
    perform_operation(10, 0)
except Exception as e:
    print(f"An unexpected error occurred in main: {e}")

try:
    perform_operation(10, "five")
except Exception as e:
    print(f"An unexpected error occurred in main: {e}")

OUTPUT :- 
Error in divide_numbers: Division by zero is not allowed.
An unexpected error occurred in perform_operation: unsupported operand type(s) for /: 'int' and 'str'
