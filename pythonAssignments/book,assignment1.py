

# 1. Book ID (int)
book_id = int(input("Enter Book ID: "))

# 2. Book Name (str)
book_name = "Wings of Fire"  # Hardcoded as per your request

# 3. Book Price (float)
price = float(input("Enter Book Price (₹): "))

# 4. Authors (list)
authors_input = input("Enter Authors (comma-separated): ")
authors = [author.strip() for author in authors_input.split(",")]

# 5. Stock Details (tuple) – Available Copies and Sold Copies
available = int(input("Enter Available Copies: "))
sold = int(input("Enter Sold Copies: "))
stock_details = (available, sold)

# 6. Discount Percentage (float)
discount = float(input("Enter Discount Percentage: "))

# 7. Book Features (set)
features_input = input("Enter Book Features (comma-separated): ")
features = set(f.strip() for f in features_input.split(","))

# 8. Publisher Info (dict)
publisher_name = input("Enter Publisher Name: ")
publisher_contact = input("Enter Publisher Contact Number: ")
publisher_location = input("Enter Publisher Location: ")
publisher_info = {
    "name": publisher_name,
    "contact": publisher_contact,
    "location": publisher_location
}

# Display Book Details Using Different Formatting Methods
print("\n" + "-"*45)
print("BOOK DETAILS FORMATTED OUTPUT")
print("-"*45)

# 1. Using Comma Separation (sep=',')
print("Book ID, Name, Price:", book_id, book_name, price, sep=", ")

# 2. Using Percentage Formatting (% operator)
print("Discount Available: %.2f%%" % discount)

# 3. Using f-strings
print(f"Book Name: {book_name}")
print(f"Book Price: ₹{price}")
print(f"Discount: {discount}%")
print(f"Stock Info: {stock_details[0]} Copies Available | {stock_details[1]} Sold")

# 4. Using .format() method
print("Publisher Info: Name - {}, Contact - {}, Location - {}".format(
    publisher_info['name'], publisher_info['contact'], publisher_info['location']
))

# Lists and Sets
print("\nAuthors:", ', '.join(authors))
print("Book Features:", ', '.join(features))
