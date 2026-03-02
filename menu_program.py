# Simple Menu Program

while True:
    print("\n1. Add")
    print("2. Subtract")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Result:", a + b)

    elif choice == "2":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Result:", a - b)

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")
