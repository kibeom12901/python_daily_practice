from art import logo

# Print the calculator logo
print(logo)

def add(n1, n2):
    """Returns the sum of two numbers."""
    return n1 + n2

def subtract(n1, n2):
    """Returns the difference of two numbers."""
    return n1 - n2

def multiply(n1, n2):
    """Returns the product of two numbers."""
    return n1 * n2

def divide(n1, n2):
    """Returns the division of two numbers."""
    if n2 == 0:
        return "Error: Division by zero."
    return n1 / n2

# Dictionary to map operations to functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    """Main calculator logic."""
    value_1 = float(input("What's the first number?: "))
    continue_calculation = True

    while continue_calculation:
        # Display available operations
        print("Available operations:")
        for key in operations:
            print(key)

        # Get the operation and next number from the user
        operation = input("Pick an operation: ")
        while operation not in operations:
            operation = input("Invalid operation. Pick a valid operation: ")
        
        value_2 = float(input("What's the next number?: "))

        # Perform the calculation
        answer = operations[operation](n1=value_1, n2=value_2)
        print(f"{value_1} {operation} {value_2} = {answer}")

        # Ask the user if they want to continue
        ask = input(f"Type 'y' to continue calculating with {answer}, or 'n' to start a new calculation: ").lower()
        if ask == 'y':
            value_1 = answer
        else:
            continue_calculation = False
            print("\n" * 2)
            print("Starting a new calculation...\n")
            calculator()
            break

# Start the calculator
calculator()
