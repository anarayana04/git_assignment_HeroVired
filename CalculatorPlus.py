import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero"

def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Error: Cannot calculate square root of a negative number"

def calculator_plus():
    print("Welcome to CalculatorPlus!")

    while True:
        print("\nChoose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Square Root")
        print("6. Exit")

        choice = input("Enter the operation number (1-6): ")

        if choice == '6':
            print("Exiting CalculatorPlus. Goodbye!")
            break

        if choice in ('1', '2', '3', '4', '5'):
            if choice == '5':
                num = float(input("Enter a number: "))
                result = square_root(num)
                print(f"Result: {result}")
            else:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))

                if choice == '1':
                    result = add(num1, num2)
                elif choice == '2':
                    result = subtract(num1, num2)
                elif choice == '3':
                    result = multiply(num1, num2)
                elif choice == '4':
                    result = divide(num1, num2)

                print(f"Result: {result}")

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    calculator_plus()