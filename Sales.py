# Below are Sales classes to be added to Final Project burger.py file as of 2025-10-06


# calculate a subtotal from an order.
class SubtotalCalculator:
    BASE_PRICES = {"Hotdog": 3.00, "Burger": 4.00}  # You can adjust these as needed
    TOPPING_PRICES = {
        "ketchup": 0.25, "mustard": 0.25, "relish": 0.40, "onion": 0.30,
        "chili": 1.00, "nacho cheese": 0.75, "cheddar": 0.50, "american": 0.50,
        "mayo": 0.25, "lettuce": 0.30, "tomato": 0.30, "pickles": 0.30,
        "bacon": 1.00, "mushrooms": 0.75, "plain": 0.00
    }

    def __init__(self, order_items):
        self.order_items = order_items

    def calculate_subtotal(self):
        subtotal = 0.0
        for item in self.order_items:
            base_price = self.BASE_PRICES.get(item["Item:"], 0.0)
            toppings = item["Toppings"]
            topping_cost = sum(self.TOPPING_PRICES.get(t.lower(), 0.0) for t in toppings)
            subtotal += base_price + topping_cost
        return round(subtotal, 2)
    

# calculate the sales tax from a subtotal
class SalesTaxCalculator:
    TAX_RATE = 0.07

    def __init__(self, subtotal):
        self.subtotal = subtotal

    def calculate_tax(self):
        return round(self.subtotal * self.TAX_RATE, 2)
    

# calculate the total from the subtotal and the sales tax
class TotalCalculator:
    def __init__(self, subtotal, tax):
        self.subtotal = subtotal
        self.tax = tax

    def calculate_total(self):
        return round(self.subtotal + self.tax, 2)


# print a receipt of items purchased, subtotal, tax, and total
class ReceiptPrinter:
    def __init__(self, order_items, subtotal, tax, total):
        self.order_items = order_items
        self.subtotal = subtotal
        self.tax = tax
        self.total = total

    def print_receipt(self):
        print("\n    Hot Dawgs Burger and Hotdog Stand\n")
        print("\n--- Receipt ---")
        for item in self.order_items:
            print(f"{item['Item:']}:")
            if item["Toppings"]:
                print("  Toppings: " + ", ".join(item["Toppings"]))
            else:
                print("  Toppings: None")
        print(f"\nSubtotal: ${self.subtotal:.2f}")
        print(f"Sales Tax (7%): ${self.tax:.2f}")
        print(f"Total: ${self.total:.2f}")
        print("--- Thank you and have a great day! ---\n")