def takeInput():
    n1 = float(input("Enter First number: "))
    n2 = float(input("Enter Second number: "))
    operator = input("Enter Operator (+,-,*,/): ")
    return n1, n2,operator 

def displayResult():
    n1, n2, operator = takeInput()

    if operator == '+':
        result = n1 + n2
        formula = f"{n1} + {n2} = {result}"
    elif operator == '-':
        result = n1 - n2
        formula = f"{n1} - {n2} = {result}"
    elif operator == '*':
        result = n1 * n2
        formula = f"{n1} * {n2} = {result}"
    elif operator == '/':
        if n2 == 0:
            print("Error")
            return
        result = n1 / n2
        formula = f"{n1} / {n2} = {result}"
    else:
        print("Invalid")
        return

    print(formula)

displayResult()



