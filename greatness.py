class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def add_item(self, item, quantity):
        if item in self.cart:
            self.cart[item] += quantity
        else:
            self.cart[item] = quantity
        return f"Added {quantity} of {item} to your cart."

    def view_cart(self):
        if not self.cart:
            return "Your cart is empty."
        items = [f"{item}: {quantity}" for item, quantity in self.cart.items()]
        return "Your cart contains:\n" + "\n".join(items)

    def checkout(self):
        if not self.cart:
            return "Your cart is empty. Cannot checkout."
        total_items = sum(self.cart.values())
        self.cart.clear()  # Clear the cart after checkout
        return f"Checked out successfully! You purchased a total of {total_items} items."


def chatbot():
    cart = ShoppingCart()
    print("Welcome to the Shopping Bot! Type 'help' for options.")

    while True:
        user_input = input("You: ").strip().lower()

        if user_input == "exit":
            print("Thank you for using the Shopping Bot. Goodbye!")
            break
        elif user_input == "help":
            print("You can use the following commands:")
            print("1. add [item] [quantity] - Add items to your cart.")
            print("2. view - View your cart.")
            print("3. checkout - Checkout your items.")
            print("4. exit - Exit the chat.")
        elif user_input.startswith("add"):
            parts = user_input.split()
            if len(parts) == 3:
                item = parts[1]
                try:
                    quantity = int(parts[2])
                    print(cart.add_item(item, quantity))
                except ValueError:
                    print("Please enter a valid quantity.")
            else:
                print("Usage: add [item] [quantity]")
        elif user_input == "view":
            print(cart.view_cart())
        elif user_input == "checkout":
            print(cart.checkout())
        else:
            print("I didn't understand that. Type 'help' for options.")


if __name__ == "__main__":
    chatbot()