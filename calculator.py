print("Welcome to the functional calculator")

#user input 
num1 = float(input("enter your 1st number: "))
num2 = float(input("enter your 2nd number: "))

print("Select operation: ")

print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")

choice = input("enter your choice (1/2/3/4): ") 
if choice == '1':
    result = num1 + num2
    print(f"result: {result}")
elif choice == '2':
    result = num1 - num2
    print(f"result: {result}")
elif choice == '3':
    result = num1 * num2
    print(f"result: {result}")
elif choice == '4':
    if num2 == 0:
        print("Error: Division by zero is not possible.")
    else:
        result = num1 / num2
        print(f"result: {result}")
else:
    print("Invalid choice. Please select a valid operation (1/2/3/4).")