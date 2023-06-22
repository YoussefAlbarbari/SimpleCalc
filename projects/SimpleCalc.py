def calculator():
    # Function to add two numbers
    def add(a, b):
        return a + b

    # Function to subtract two numbers
    def subtract(a, b):
        return a - b

    # Function to divide two numbers, handles division by zero error
    def divide(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            print("Error: Division by zero.")
            return None

    # Function to multiply two numbers
    def multiply(a, b):
        return a * b

    # Function to calculate the percentage of a value
    def calculate_percentage(value, percentage):
        return value * (percentage / 100)

    # Function to calculate the percentage change between two values
    def calculate_percentage_change(old_value, new_value):
        try:
            return ((new_value - old_value) / old_value) * 100
        except ZeroDivisionError:
            print("Error: Division by zero.")
            return None

    # Function to clear the result (currently not used)
    def clear_result():
        result_label = ""

    # Function to perform the calculation based on user input
    def calculate():
        operations = operation_var.get()  # Get the selected operation from user input
        num1 = num1_entry.get()  # Get the first number from user input
        num2 = num2_entry.get()  # Get the second number from user input

        if not num1.isdigit() or not num2.isdigit():
            # Check if the input numbers are valid (numeric)
            print("Error: Invalid input. Numbers must be numeric.")
            return

        num1 = float(num1)  # Convert the first number to a float
        num2 = float(num2)  # Convert the second number to a float
        result = ""  # Initialize the result variable as an empty string

        # Perform the corresponding operation based on user input
        if operations == "add":
            result = add(num1, num2)
        elif operations == "sub" or operations == "subtract":
            result = subtract(num1, num2)
        elif operations == "div" or operations == "divide":
            result = divide(num1, num2)
        elif operations == "mul" or operations == "multiply":
            result = multiply(num1, num2)
        elif operations == "percentage":
            result = calculate_percentage(num1, num2)
        elif operations == "percentage_change":
            result = calculate_percentage_change(num1, num2)
        else:
            print("Error: Invalid operation.")
            return

        if result is not None:
            print("Result:", result)  # Print the calculated result

    # Welcome message and available operations
    print("Welcome to the simple calculator")
    print("add   subtract   divide   multiply   percentage   percentage_change")

    # User input for numbers and operation
    num1_entry = input("Enter the first number: ")
    num2_entry = input("Enter the second number: ")
    operation_var = input("Choose the operation: ")

    calculate()  # Call the calculate() function to perform the calculation

# Call the calculator function to start the program
calculator()
