# SimpleCalc
Effortless calculations made simple. SimpleCalc is a sleek and intuitive calculator app built to handle your everyday math tasks with ease. From basic arithmetic to percentage calculations, it's your go-to tool for quick and accurate results. Experience hassle-free computation at your fingertips!


# Introduction:
"Welcome to my simple calculator project! This calculator was designed with one goal in mind: to provide users with a fast and efficient tool for performing basic mathematical calculations. While there are numerous calculators available, our calculator stands out by offering a clean and intuitive user interface coupled with a seamless user experience. Whether you're a student, professional, or anyone in need of quick calculations, our calculator is here to simplify your math tasks."

# Value proposition and unique benefits:

Time-saving convenience: "With our calculator, you no longer have to waste time manually performing calculations on paper or searching for a physical calculator. Our digital tool allows you to swiftly input your numbers and operators, providing instant results at your fingertips."

Error-free accuracy: "Eliminate the risk of manual calculation errors. Our calculator ensures accurate results, reducing the chances of mistakes that can often occur when performing calculations manually."

User-friendly design: "We understand the importance of a user-friendly interface. Our calculator features a clean and intuitive design, making it easy for anyone, regardless of their mathematical background, to use and navigate effortlessly."

Portability and accessibility: "Access our calculator anytime, anywhere, using any device with internet connectivity. Whether you're on your computer, tablet, or smartphone, our calculator is readily available, making it a versatile tool for on-the-go calculations."

# Explain the code

def calculator():

  Purpose: This function serves as the entry point of the calculator program. It prompts the user for input and calls the necessary functions to perform calculations.
  Inputs: None
  Outputs: None

def add(a, b):

  Purpose: This function performs addition of two numbers.
  Inputs: Two numbers a and b.
  Outputs: The sum of a and b.

def subtract(a, b):

  Purpose: This function performs subtraction of two numbers.
  Inputs: Two numbers a and b.
  Outputs: The result of subtracting b from a.

def divide(a, b):

  Purpose: This function performs division of two numbers, handling the division by zero error.
  Inputs: Two numbers a and b.
  Outputs: The result of dividing a by b. If b is zero, it prints an error message and returns None.

def multiply(a, b):

  Purpose: This function performs multiplication of two numbers.
  Inputs: Two numbers a and b.
  Outputs: The product of a and b.

def calculate_percentage(value, percentage):

  Purpose: This function calculates the percentage of a value.
  Inputs: A numeric value and a percentage value.
  Outputs: The calculated percentage of value.

def calculate_percentage_change(old_value, new_value):

  Purpose: This function calculates the percentage change between two values.
  Inputs: Two numeric values old_value and new_value.
  Outputs: The percentage change from old_value to new_value. If old_value is zero, it prints an error message and returns None.

def clear_result():

  Purpose: This function clears the result (currently not used in the code).
  Inputs: None
  Outputs: None

def calculate():

  Purpose: This function performs the calculation based on user input. It calls the appropriate functions to execute the selected operation.
  Inputs: None (retrieves inputs from user during function execution)
  Outputs: None (prints the calculated result or error messages)

The code block below the calculate() function performs the following tasks:

  Prints a welcome message and displays the available operations.
  Prompts the user to enter the first number, second number, and the desired operation.
  Calls the calculate() function to perform the calculation based on user input.
  The final line outside any function calculator() calls the calculator() function to start the program execution.

 # Usage Instructions:

Run the calculator program.

You will be greeted with a welcome message and a list of available operations: add, subtract, divide, multiply, percentage, percentage_change.

Enter the first number when prompted: [Enter the first number]

Enter the second number when prompted: [Enter the second number]

Choose the operation by entering the corresponding keyword (e.g., add, subtract, divide) or its abbreviation (e.g., mul for multiply).

The program will calculate the result based on the provided numbers and the chosen operation.

The calculated result will be displayed: Result: [calculated result].

You can perform additional calculations by running the calculator program again.


Examples:

  Addition: Adding two numbers.
	
Enter the first number: 5
Enter the second number: 3
Choose the operation: add
Result: 8



  Division: Dividing two numbers.

Enter the first number: 10
Enter the second number: 2
Choose the operation: divide
Result: 5.0

Percentage: Calculating the percentage of a value.

Enter the first number: 80
Enter the second number: 25
Choose the operation: percentage
Result: 20.0

Invalid input: Providing non-numeric input for numbers.

Enter the first number: abc
Error: Invalid input. Numbers must be numeric.

Invalid operation: Choosing an invalid operation.

Enter the first number: 5
Enter the second number: 3
Choose the operation: power
Error: Invalid operation.
