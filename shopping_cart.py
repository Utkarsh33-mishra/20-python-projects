#  online shopping cart
cart = ["Apple", "Guava", "Banana"]


def view_cart():
    if len(cart) == 0:
        print("\n🛒 Cart is empty.")
    else:
        print("\n🛒 Your Cart:")
        for index, item in enumerate(cart, start=1):
            print(f"{index}. {item}")


def add_item():
    item = input("Enter item to add: ")

    if item in cart:
        print(f"{item} is already in the cart.")
    else:
        cart.append(item)
        print(f"{item} added successfully.")


def remove_item():
    item = input("Enter item to remove: ")

    if item in cart:
        cart.remove(item)
        print(f"{item} removed successfully.")
    else:
        print("Item not found.")


def update_item():
    old_item = input("Enter the item to update: ")

    if old_item in cart:
        new_item = input("Enter the new item: ")
        index = cart.index(old_item)
        cart[index] = new_item
        print("Item updated successfully.")
    else:
        print("Item not found.")


def clear_cart():
    cart.clear()
    print("Cart cleared successfully.")


def menu():
    while True:
        print("\n========== Shopping Cart ==========")
        print("1. View Cart")
        print("2. Add Item")
        print("3. Remove Item")
        print("4. Update Item")
        print("5. Clear Cart")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_cart()

        elif choice == "2":
            add_item()

        elif choice == "3":
            remove_item()

        elif choice == "4":
            update_item()

        elif choice == "5":
            clear_cart()

        elif choice == "6":
            print("🛍️ Thank you for shopping!")
            break

        else:
            print("❌ Invalid choice. Please try again.")


menu()


    

                
    