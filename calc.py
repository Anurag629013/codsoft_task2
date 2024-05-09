def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def division(x, y):
    return x / y

while True:
    print("Select operation to be performed.\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")  
    c = input("Enter your choice ( 1      2       3       4 ) : ")
    if c in ('1', '2', '3', '4'):
        try:
            n1 = float(input("Enter the first number: "))
            n2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if c == '1':
            print(n1, "+", n2, "=", add(n1, n2))

        elif c == '2':
            print(n1, "-", n2, "=", subtract(n1, n2))

        elif c == '3':
            print(n1, "*", n2, "=", multiply(n1, n2))

        elif c == '4':
            if n2 == 0:
                print("Cannot divide by zero.")
                continue
            print(n1, "/", n2, "=", division(n1, n2))

        nextcal = input("Want to Continue calculation? (yes/no): ")
        if (nextcal == "no") or (nextcal == "n") or (nextcal == "NO") or (nextcal == "N") or (nextcal == "No"):
            break
    else:
        print("Invalid Input!")
