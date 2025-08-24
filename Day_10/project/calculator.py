import art

print(art.logo)


first_num = int(input("What's the first number?: "))
operation_sign = input("+\n-\n*\n/\nPick an operation: ")
second_num = int(input("What's the next number?: "))


def calculator(n1, operation, n2):
    if operation == "+":
        return n1 + n2
    elif operation == "-":
        return n1 - n2
    elif operation == "*":
        return n1 * n2
    elif operation == "/":
        if n2 != 0:
            return n1 / n2
        else:
            return "Error: Division by zero!"
    else:
        return "Invalid operation"


print(calculator(first_num, operation_sign, second_num))
