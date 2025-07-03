def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

while True:
    print("\nSelect operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Exit")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '5':
        print("\nExiting calculator. Goodbye!")
        break

    if choice not in ['1', '2', '3', '4']:
        print("\nInvalid input! Please try again.")
        continue

    try:
        num1 = float(input("\nEnter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid number! Please enter numeric values.")
        continue

    if choice == '1':
        print("\nResult:", add(num1, num2))
    elif choice == '2':
        print("\nResult:", subtract(num1, num2))
    elif choice == '3':
        print("\nResult:", multiply(num1, num2))
    elif choice == '4':
        print("\nResult:", divide(num1, num2))
