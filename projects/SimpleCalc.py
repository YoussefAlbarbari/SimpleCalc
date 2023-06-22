def calculator():
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def divide(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            print("Error: Division by zero.")
            return None

    def multiply(a, b):
        return a * b

    def calculate_percentage(value, percentage):
        return value * (percentage / 100)

    def calculate_percentage_change(old_value, new_value):
        try:
            return ((new_value - old_value) / old_value) * 100
        except ZeroDivisionError:
            print("Error: Division by zero.")
            return None

    def clear_result():
        result_label = ""

    def calculate():
        operations = operation_var.get()
        num1 = num1_entry.get()
        num2 = num2_entry.get()

        if not num1.isdigit() or not num2.isdigit():
            print("Error: Invalid input. Numbers must be numeric.")
            return

        num1 = float(num1)
        num2 = float(num2)
        result = ""

        if operations == "add":
            result = add(num1, num2)
        elif operations == "sub" or operations == "subtract":
            result = subtract(num1, num2)
        elif operations == "div" or operations == "divide":
            result = divide(num1, num2)
        elif operations == "mul"or operations == "multiply":
            result = multiply(num1, num2)
        elif operations == "percentage":
            result = calculate_percentage(num1, num2)
        elif operations == "percentage_change":
            result = calculate_percentage_change(num1, num2)
        else:
            print("Error: Invalid operation.")
            return

        if result is not None:
            print("Result:", result)

    print("Welcome to the simple calculator")
    print("add   subtract   divide   multiply   percentage   percentage_change")

    num1_entry = input("Enter the first number: ")
    num2_entry = input("Enter the second number: ")
    operation_var = input("Choose the operation: ")

    calculate()

# Call the calculator function to start the program
calculator()
