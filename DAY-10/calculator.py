import art


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


maths = {"+": add, "-": sub, "*": mul, "/": div}


def calculator():
    print(art.logo)
    should_continue = True
    n1 = float(input("What's the first number? "))
    while should_continue:
        for symbol in maths:
            print(symbol)
        operation = input("Pick an operation ")
        n2 = float(input("What's the second number? "))
        outcome = float(f"{maths[operation](n1, n2)}")
        result = f"{n1} {operation} {n2} = {outcome}"
        print(result)

        continue_cal = input(
            f"Type 'y' to continue with {outcome}, or type 'n' to start a new calculation: "
        ).lower()
        if continue_cal == "y":
            n1 = outcome
        else:
            should_continue = False
            print("\n" * 20)
            calculator()


calculator()
