def add(x, y):
    """Function to add two numbers."""
    return x + y

def subtract(x, y):
    """Function to subtract two numbers."""
    return x - y



def main():
    """Main function to demonstrate the usage of other functions."""
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("1. Addition")
    print("2. Subtraction")
    

    choice = input("Enter choice (1/2/3/4): ")

    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    else:
        print("Invalid input")

if __name__ == "__main__":
    main()
