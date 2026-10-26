# Import the datetime module to work with dates and times
import datetime

# Create a list containing all available product names
products = ["Chetos", "Soda", "Dulce", "Cookies", "Agua", "Sandwich"]

# Create a list containing the prices of the products in the same order
prices = [2.00, 2.50, 1.50, 3.00, 1.00, 5.00]

# Create an empty list to store the products added to the shopping cart
shopping_cart = []

# Initialize the user's menu choice to 0
user_choice = 0


# Define a function to display all available products
def display_products():
    # Print a heading for the available products
    print("========== AVAILABLE PRODUCTS ==========")

    # Loop through the indexes of the products list
    for i in range(len(products)):
        # Display the product number, name, and price
        # i + 1 makes the displayed numbering start at 1 instead of 0
        # :12 reserves 12 character spaces for the product name
        # :.2f formats the price to two decimal places
        print(f"{i + 1}. {products[i]:12} ${prices[i]:.2f}")


# Define a function to add a product to the shopping cart
def add_product():
    # Display the list of available products
    display_products()

    # Ask the user for a product number and convert the input to an integer
    product_number = int(input("Enter product number: "))

    # Repeat while the entered number is less than 1 or greater than the number of products
    while product_number < 1 or product_number > len(products):
        # Inform the user that the selected product number is invalid
        print("Invalid product!")

        # Tell the user which product numbers are allowed
        print("Please choose a number between 1 and 6.")

        # Ask the user to enter another product number
        product_number = int(input("Enter product number: "))

    # Get the selected product from the list
    # Subtract 1 because Python list indexes start at 0
    product = products[product_number - 1]

    # Add the selected product name to the shopping cart list
    shopping_cart.append(product)

    # Confirm that the product was successfully added
    print(f"{product} was added to your cart!")


# Define a function to remove one selected item from the shopping cart
def remove_product():
    # Check whether the shopping cart is empty
    if len(shopping_cart) == 0:
        # Inform the user that the cart is empty
        print("Your shopping cart is empty!")

        # Explain that there are no items available to remove
        print("There is nothing to remove.")

        # Stop the function because there is nothing to remove
        return

    # Display the current items in the shopping cart
    display_cart()

    # Ask the user which item number they want to remove
    # Convert the entered text into an integer
    item_number = int(input("Which item would you like to remove? "))

    # Repeat while the item number is outside the valid range
    while item_number < 1 or item_number > len(shopping_cart):
        # Inform the user that the selected item does not exist
        print("That item does not exist in your cart!")

        # Ask the user to enter another item number
        item_number = int(input("Enter item number: "))

    # Remove the selected item from the cart and store its name
    # Subtract 1 because list indexes start at 0
    removed_item = shopping_cart.pop(item_number - 1)

    # Inform the user which product was removed
    print(f"{removed_item} was removed from your cart!")


# Define a function to calculate the subtotal of all items in the cart
def calculate_total():
    # Initialize the total price to zero
    total = 0

    # Loop through every product in the shopping cart
    for item in shopping_cart:
        # Find the index of the current product in the products list
        index = products.index(item)

        # Add the price at the matching index to the running total
        total += prices[index]

    # Return the calculated subtotal to the function that called this function
    return total


# Define a function to display all items in the shopping cart
def display_cart():
    # Print a heading for the shopping cart
    print ("========== YOUR SHOPPING CART ==========")

    # Check whether the shopping cart is empty
    if len(shopping_cart) == 0:
        # Inform the user that there are no items in the cart
        print("Your shopping cart is empty!")

        # Stop the function because there are no items to display
        return

    # Loop through the indexes of all items in the shopping cart
    for i in range(len(shopping_cart)):
        # Get the item at the current shopping cart index
        item = shopping_cart[i]

        # Find the item's index in the original products list
        index = products.index(item)

        # Display the item number, product name, and price
        # i + 1 displays item numbers starting at 1
        # :12 aligns the product names
        # :.2f formats the price to two decimal places
        print(f"{i + 1}. {item:12} ${prices[index]:.2f}")

    # Display the total number of items in the shopping cart
    print(f"Total Items: {len(shopping_cart)}")


# Define a function to display the current subtotal
def display_total():
    # Print a heading for the current total
    print("========== CURRENT TOTAL ==========")

    # Check whether the shopping cart is empty
    if len(shopping_cart) == 0:
        # Inform the user that the cart is empty
        print("Your shopping cart is empty!")

        # Stop the function because there is no total to display
        return

    # Loop through every item in the shopping cart
    for item in shopping_cart:
        # Find the current item's index in the products list
        index = products.index(item)

        # Display the product name and its corresponding price
        print(f"{item:12} ${prices[index]:.2f}")

    # Call calculate_total() and store its returned subtotal
    subtotal = calculate_total()

    # Display the subtotal formatted to two decimal places
    print(f"Subtotal: ${subtotal:.2f}")


# Define a function to determine the discount rate based on the subtotal
def calculate_discount(subtotal):
    # If the subtotal is less than $10, give no discount
    if subtotal < 10:
        # Set the discount rate to 0%
        discount_rate = 0

    # If the subtotal is at least $10 but less than $20, give 5% off
    elif subtotal < 20:
        # Store 5% as a decimal value
        discount_rate = 0.05

    # If the subtotal is at least $20 but less than $40, give 10% off
    elif subtotal < 40:
        # Store 10% as a decimal value
        discount_rate = 0.10

    # If the subtotal is $40 or more, give 15% off
    else:
        # Store 15% as a decimal value
        discount_rate = 0.15

    # Return the discount rate to the function that called this function
    return discount_rate


# Define a function to complete checkout and print the final receipt
def checkout():
    # Check whether the shopping cart is empty
    if len(shopping_cart) == 0:
        # Inform the user that the cart is empty
        print("Your shopping cart is empty!")

        # Tell the user to add products before checking out
        print("Add some products before checking out.")

        # Return False to indicate that checkout did not complete
        return False

    # Calculate the subtotal before applying any discounts
    subtotal = calculate_total()

    # Determine the discount rate based on the subtotal
    discount_rate = calculate_discount(subtotal)

    # Calculate the amount of money saved by applying the discount
    amount_saved = subtotal * discount_rate

    # Subtract the discount amount from the subtotal to get the final total
    final_total = subtotal - amount_saved

    # Get the current date and format it as month/day/year
    current_date = datetime.datetime.now().strftime("%m/%d/%Y")

    # Print the heading for the receipt
    print("========== RECEIPT ==========")

    # Display the current date on the receipt
    print(f"Date: {current_date}")

    # Print a separator line
    print("--------------------------------")

    # Loop through every item in the shopping cart
    for item in shopping_cart:
        # Find the item's index in the original products list
        index = products.index(item)

        # Print the product name and its price
        print(f"{item:12} ${prices[index]:.2f}")

    # Print another separator line
    print("--------------------------------")

    # Display the subtotal before the discount
    print(f"Subtotal:       ${subtotal:.2f}")

    # Display the discount as a percentage with no decimal places
    # For example, 0.10 is displayed as 10%
    print(f"Discount:       {discount_rate:.0%}")

    # Display the amount of money saved
    print(f"Amount Saved:   ${amount_saved:.2f}")

    # Display the final amount the customer must pay
    print(f"Final Total:    ${final_total:.2f}")

    # Thank the customer for shopping
    print("Thank you for shopping!")

    # Return True to indicate that the receipt was printed successfully
    return True


# Start the main menu loop and continue while the user's choice is not 6
while user_choice != 6:
    # Print the title of the shopping cart menu
    print("========== SMART SHOPPING CART ==========")

    # Display option 1 for viewing available products
    print("1. View Available Products")

    # Display option 2 for adding a product to the cart
    print("2. Add Product to Cart")

    # Display option 3 for removing a product from the cart
    print("3. Remove Product from Cart")

    # Display option 4 for viewing the shopping cart
    print("4. View Shopping Cart")

    # Display option 5 for viewing the current subtotal
    print("5. View Current Total")

    # Display option 6 for checking out
    print("6. Checkout")

    # Ask the user to select a menu option and convert it to an integer
    user_choice = int(input("Enter your choice: "))

    # Repeat while the menu choice is less than 1 or greater than 6
    while user_choice < 1 or user_choice > 6:
        # Inform the user that the selected menu option is invalid
        print("Invalid option!")

        # Ask the user to enter a valid menu option
        user_choice = int(input("Enter your choice: "))

    # If the user selects option 1, display the available products
    if user_choice == 1:
        # Call the function that displays all products and prices
        display_products()

    # If the user selects option 2, add a product to the cart
    elif user_choice == 2:
        # Call the function that handles adding a product
        add_product()

    # If the user selects option 3, remove an item from the cart
    elif user_choice == 3:
        # Call the function that handles removing an item
        remove_product()

    # If the user selects option 4, display the shopping cart
    elif user_choice == 4:
        # Call the function that displays all cart items
        display_cart()

    # If the user selects option 5, display the current subtotal
    elif user_choice == 5:
        # Call the function that displays item prices and the subtotal
        display_total()

    # If the user selects option 6, attempt to check out
    elif user_choice == 6:
        # Check whether the shopping cart is empty
        if len(shopping_cart) == 0:
            # Inform the user that the shopping cart is empty
            print("Your shopping cart is empty!")

            # Tell the user to add products before checking out
            print("Add some products before checking out.")

            # Reset the choice to 0 so the main menu appears again
            # Because 0 is not 6, the outer while loop continues
            user_choice = 0

        # If the cart contains items, proceed with checkout
        else:
            # Calculate the total, apply the discount, and print the receipt
            checkout()