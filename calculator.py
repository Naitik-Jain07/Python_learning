def add(n1,n2):
    return n1 + n2
def subtract(n1,n2):
    return n1- n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

operators={
    "+" : add ,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}
# print(operators["*"](4,5))
def calculator() :
    should_continue = True
    num1 = float(input("whats first number ?: "))
    while should_continue:
    
        for operator in operators:
            print(operator)
        operation = (input("pick an operator"))
        num2 = float(input("whats second number ?: "))
        answer = (operators[operation](num1,num2))
        print(f"{num1} {operation} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start new calculation")

        if choice == 'y':
            num1 = answer
        else :
            should_continue = False
            print("\n" * 20)
            calculator()

calculator()


