def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    return x / y

while True:
    print("Select operation.\n1.Add\n2.Subtract\n3.Multiply\n4.Divide")  
    c = input("Enter choice ( 1      2       3       4 ) : ")
    if c in ('1', '2', '3', '4'):
        try:
            n1 = float(input("Enter first number: "))
            n2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if c == '1':
            print(n1, "+", n2, "=", add(n1, n2))

        elif c == '2':
            print(n1, "-", n2, "=", sub(n1, n2))

        elif c == '3':
            print(n1, "*", n2, "=", mult(n1, n2))

        elif c == '4':
            if n2 == 0:
                print("Cannot divide by zero.")
                continue
            print(n1, "/", n2, "=", div(n1, n2))

        nextcal = input("Let's do next calculation? (yes/no): ")
        if (nextcal == "no") or (nextcal == "n") or (nextcal == "NO") or (nextcal == "N") or (nextcal == "No"):
            break
    else:
        print("Invalid Input")