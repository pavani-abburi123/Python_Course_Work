import random

print("===== Welcome to Python Zepto =====")

users = []

categories = {
    "Dairy": [
        {"id": 1, "item": "Milk", "price": 60},
        {"id": 2, "item": "Cheese", "price": 120},
        {"id": 3, "item": "Curd", "price": 100},
        {"id": 4, "item": "Butter", "price": 90},
    ],
    "Bakery": [
        {"id": 5, "item": "Bread", "price": 40},
        {"id": 6, "item": "Buns", "price": 30},
        {"id": 7, "item": "Cakes", "price": 120},
        {"id": 8, "item": "Croissant", "price": 55},
    ],
    "Fruits": [
        {"id": 9, "item": "Apple", "price": 100},
        {"id": 10, "item": "Banana", "price": 50},
        {"id": 11, "item": "Mango", "price": 180},
        {"id": 12, "item": "Grapes", "price": 90},
    ],
    "Vegetables": [
        {"id": 13, "item": "Tomato", "price": 30},
        {"id": 14, "item": "Potato", "price": 25},
        {"id": 15, "item": "Onion", "price": 35},
        {"id": 16, "item": "Carrot", "price": 40},
    ],
    "Snacks & Beverages": [
        {"id": 17, "item": "Chips", "price": 20},
        {"id": 18, "item": "Biscuits", "price": 35},
        {"id": 19, "item": "Soft Drink", "price": 45},
        {"id": 20, "item": "Juice", "price": 55},
    ],
    "Personal Care": [
        {"id": 21, "item": "Shampoo", "price": 120},
        {"id": 22, "item": "Toothpaste", "price": 60},
        {"id": 23, "item": "Soap", "price": 35},
        {"id": 24, "item": "Face Wash", "price": 150},
    ],
    "Household Essentials": [
        {"id": 25, "item": "Detergent", "price": 180},
        {"id": 26, "item": "Dishwash Gel", "price": 90},
        {"id": 27, "item": "Toilet Cleaner", "price": 110},
        {"id": 28, "item": "Room Freshener", "price": 140},
    ],
    "Baby Care": [
        {"id": 29, "item": "Baby Diapers", "price": 350},
        {"id": 30, "item": "Baby Lotion", "price": 220},
        {"id": 31, "item": "Baby Food", "price": 180},
        {"id": 32, "item": "Baby Soap", "price": 90},
    ],
    "Frozen Foods": [
        {"id": 33, "item": "Frozen Peas", "price": 75},
        {"id": 34, "item": "Ice Cream", "price": 60},
        {"id": 35, "item": "Frozen Paratha", "price": 100},
        {"id": 36, "item": "Nuggets", "price": 150},
    ]
}

delivery_boys = ["Aryan", "Meera", "Kabir", "Zara"]
basket = []
order_history = []

logged_in = False
current_user = None

# Login/Register
while not logged_in:
    print("\n1. Register\n2. Login")
    ch = input("Select option: ")

    if ch == "1":
        uname = input("New username: ")
        pwd = input("New password: ")
        exists = False
        for u in users:
            if u["username"] == uname:
                exists = True
                break
        if exists:
            print("Username exists. Try another.")
        else:
            users.append({"username": uname, "password": pwd})
            print("Registered. Please login.")

    elif ch == "2":
        uname = input("Username: ")
        pwd = input("Password: ")
        for u in users:
            if u["username"] == uname and u["password"] == pwd:
                current_user = u
                logged_in = True
                print("Login successful. Welcome", uname)
                break
        if not logged_in:
            print("Invalid credentials.")

# Main Dashboard
while True:
    print("\n===== Zepto Dashboard =====")
    print("1. View Categories")
    print("2. View Basket")
    print("3. Remove from Basket")
    print("4. Checkout")
    print("5. Logout")
    print("6. Search Products")
    print("7. View Order History")
    print("8. Clear Basket")
    print("9. Exit App")

    op = input("Select an option: ")

    if op == "1":
        print("\n--- Product Categories ---")
        cat_list = list(categories.keys())
        for i in range(len(cat_list)):
            print(i+1, "-", cat_list[i])
        cat_choice = int(input("Select category by number: "))
        if 1 <= cat_choice <= len(cat_list):
            selected_cat = cat_list[cat_choice - 1]
            print("\n---", selected_cat, "Items ---")
            items = categories[selected_cat]
            for item in items:
                print(item["id"], "-", item["item"], "| ₹", item["price"])

            while True:
                item_id = int(input("Enter item ID to add to basket (0 to stop): "))
                if item_id == 0:
                    break
                added = False
                for item in items:
                    if item["id"] == item_id:
                        basket.append(item)
                        print(item["item"], "added to basket.")
                        added = True
                        break
                if not added:
                    print("Invalid item ID.")
        else:
            print("Invalid category.")

    elif op == "2":
        print("\n--- Your Basket ---")
        if not basket:
            print("Basket is empty.")
        else:
            total = 0
            for item in basket:
                print(item["item"], "| ₹", item["price"])
                total += item["price"]
            print("Total Amount: ₹", total)

    elif op == "3":
        print("\n--- Remove Items from Basket ---")
        if not basket:
            print("Basket is empty.")
        else:
            for i, item in enumerate(basket):
                print(i+1, "-", item["item"], "| ₹", item["price"])
            remove_index = int(input("Enter item number to remove (0 to cancel): "))
            if 1 <= remove_index <= len(basket):
                removed_item = basket.pop(remove_index - 1)
                print(removed_item["item"], "removed from basket.")
            elif remove_index == 0:
                print("Cancelled.")
            else:
                print("Invalid selection.")

    elif op == "4":
        print("\n--- Checkout ---")
        if not basket:
            print("Basket is empty.")
        else:
            total = 0
            for item in basket:
                print(item["item"], "| ₹", item["price"])
                total += item["price"]
            print("Total bill: ₹", total)
            pay = input("Pay now? (yes/no): ")
            if pay.lower() == "yes":
                print("Payment successful!")
                delivery = random.choice(delivery_boys)
                print("Order placed successfully. Your delivery partner is", delivery)
                order_history.append(basket.copy())
                basket.clear()
            else:
                print("Payment cancelled.")

    elif op == "5":
        print("Logged out.")
        break

    elif op == "6":
        query = input("Enter product name to search: ").lower()
        found = False
        for cat, items in categories.items():
            for item in items:
                if query in item["item"].lower():
                    print(f"{item['item']} (₹{item['price']}) - Category: {cat}")
                    found = True
        if not found:
            print("No items matched your search.")

    elif op == "7":
        print("\n--- Order History ---")
        if not order_history:
            print("No past orders.")
        else:
            for i, order in enumerate(order_history):
                print(f"\nOrder {i+1}:")
                for item in order:
                    print(f"  - {item['item']} (₹{item['price']})")

    elif op == "8":
        if not basket:
            print("Basket is already empty please add items if u want.")
        else:
            basket.clear()
            print("Basket cleared.")

    elif op == "9":
        print("Thank you for using Python Zepto. Goodbye!")
        exit()

    else:
        print("Invalid option.")
