# Nested If-Else Example

age = int(input("Enter your age: "))
has_id = input("Do you have an ID? (yes/no): ").lower()

if age >= 18:
    if has_id == "yes":
        print("You are allowed to enter.")
    else:
        print("You need an ID to enter.")
else:
    print("You are underage.")
