from art import logo

print(logo)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = int(input("What's the first number?: "))

for symbol in operations:
    print(symbol)


def calculator(n1, n2, operation):
    answer = operations[operation](n1, n2)
    return answer


continue_calculation = True

while continue_calculation:
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = int(input("What's the next number?: "))
    result = calculator(num1, num2, operation_symbol)
    print(f"{num1} {operation_symbol} {num2} = {result}")

    user_input = input(f"Type 'y' to continue calculating with {result}, or type 'n' to quit: ")

    if user_input == "y":
        num1 = result
    else:
        continue_calculation = False
