def calculator():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Choose (+, -, *, /, %, **): ")

        if operation == '+':
            print(num1 + num2)
        elif operation == '-':
            print(num1 - num2)
        elif operation == '*':
            print(num1 * num2)
        elif operation == '/':
            print(num1 / num2 if num2 != 0 else "Error: Divide by Zero")
        elif operation == '%':
            print(num1 % num2)
        elif operation == '**':
            print(num1 ** num2)
        else:
            print("Invalid operation")
    except ValueError:
        print("Invalid input! Please enter numbers.")

calculator()
