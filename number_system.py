number = input("Enter a number: ")

while not number.isdigit():
    print("Please enter a valid number.")
    number = input("Enter a number: ")

number = int(number)

print("1. Forward")
print("2. Backward")
print("3. Vertical")
print("4. Horizontal")

choice = input("How would you like to display the number? Enter the corresponding number: ")

if choice == "1":
    print("Forward:", number)
elif choice == "2":
    print("Backward:", str(number)[::-1])
elif choice == "3":
    for i in str(number):
        print(i)
elif choice == "4":
    print("Horizontal:", " ".join(str(f) for f in str(number)))
else:
    print("Invalid choice. Please try again.")