inventory = {}

while True:
    print("\n1. Add item to inventory")
    print("2. Remove item from inventory")
    print("3. Display inventory")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        item_name = input("Enter the name of the item: ")
        item_quantity = int(input("Enter the quantity of the item: "))
        if item_name in inventory:
            inventory[item_name] += item_quantity
        else:
            inventory[item_name] = item_quantity
        print(f"{item_quantity} {item_name}(s) added to inventory.")
    elif choice == '2':
        item_name = input("Enter the name of the item to remove: ")
        if item_name in inventory:
            item_quantity = int(input("Enter the quantity to remove: "))
            if item_quantity >= inventory[item_name]:
                del inventory[item_name]
            else:
                inventory[item_name] -= item_quantity
            print(f"{item_quantity} {item_name}(s) removed from inventory.")
        else:
            print(f"{item_name} not found in inventory.")
    elif choice == '3':
        print("Inventory:")
        for item, quantity in inventory.items():
            print(f"{item}: {quantity}")
    elif choice == '4':
        print("Exiting the inventory system. Thank you!")
        break
    else:
        print("Invalid choice. Please try again.")