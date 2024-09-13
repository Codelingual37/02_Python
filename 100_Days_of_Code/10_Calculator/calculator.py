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


previous = 0

calculator = {

    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide

}

repeat = False

while True:
    if previous == 0:
        first = int(input("What is the first number? "))
    else:
        first = previous
    operator = input("Which mathematical operator do you want? (Type '+', '-', '*', or '/') ")
    second = int(input("What is the second number? "))
    result = calculator[operator](first, second)
    print(f"{first} {operator} {second} = {result}")
    more_calc = input("Do you want to do another calculation with this result? (type 'yes' or 'no') ").lower()
    if more_calc == "yes":
        previous += result
    else:
        previous = 0
