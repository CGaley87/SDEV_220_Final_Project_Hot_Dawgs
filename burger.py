from enum import Enum

class FoodToppings(Enum):
    cheddar = 1
    american = 2
    ketchup = 3 
    mustard = 4
    mayo = 5
    lettuce  = 6
    tomato = 7
    onion = 8
    pickles = 9
    bacon = 10
    mushrooms = 11
    relish = 12
    plain = 13


class Menu():
    PRICES = {
        "base": 
        {"regular": 3.00, "chicago": 4.50, "coney": 4.25
        },
        "toppings": 
        {
            "ketchup": 0.25, "mustard": 0.25, "relish": 0.40, "onions": 0.30,
             "chili": 1.00, "nacho cheese": 0.75
        }
    }
    def __init__(self, hotdog, burger, side):
        self.hotdog = hotdog
        self.burger = burger
        self.side = side
        
    
        
class Order(Menu):
    def __init__(self, hotdog, burger, side):
        super().__init__(hotdog, burger, side)
        self.order = []
        

    def getOrder(self):
        print("Choose an option from below (Press 0 to stop order):")
        print ("1. Hotdog")
        print ("2. Burger")
        print ("3. Side")
        while True:
            foodChoice = input("Enter your choice: ")
            if foodChoice == '0':
                break

            elif foodChoice == '1' and self.hotdog:
             itemToppings = self.getToppings()
             self.order.append({"Item:": "Hotdog", "Toppings": itemToppings})
             
            

            elif foodChoice == '2' and self.burger:
            
                itemToppings = self.getToppings()
                self.order.append({"Item:": "Burger", "Toppings": itemToppings})
            
            
            elif foodChoice == '3' and self.side:
            # Call Side class to handle side order
                print("Side ordering not yet implemented.")
            else:
                print("Invalid choice or option not available.")


    def getToppings(self):
        toppings = [] 
        print("Toppings available: (Enter 13 for plain)")
        print("1. Cheddar")
        print("2. American")
        print("3. Ketchup")
        print("4. Mustard")
        print("5. Mayo")
        print("6. Lettuce")
        print("7. Tomato")
        print("8. Onion")
        print("9. Pickles")
        print("10. Bacon")
        print("11. Mushrooms")
        print("12. Relish")
        print("13. Plain")

        while True:
            topping_choice = input("Enter topping numbers: (0 to finish) ")
            if topping_choice == '0':
                break
            if topping_choice == '13': #This is for if they get it plain, makes the toppings empty and adds plain and exits loop
                toppings = []
                topping_choice = FoodToppings(int(topping_choice))
                toppings.append(topping_choice.name)
                break
            try:
                topping_choice = FoodToppings(int(topping_choice))
                toppings.append(topping_choice.name)
                
            except ValueError:
                print("Invalid topping choice. Please try again.")
        return toppings
            




    


#Display that loops until a valid choice is made
def display_menu():
    while True:
        print("The Hot-Dawgs Menu:")
        print("1. Start a new order")
        print("2. View daily sales report")
        menu_choice = input("Enter your choice: ").strip()
        if menu_choice in ['1', '2']:
            return menu_choice
            break

        else:
            print("Invalid choice. Please enter 1 or 2.")
        

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


def main():
    allOrders = []
    menu = Menu( hotdog=True, burger=True, side=True)
    while True:    
        #While loop to keep displaying menu until user exits                                     
        menu_choice = display_menu()
    
        if menu_choice == '1':
    
            order = Order(menu.hotdog, menu.burger, menu.side)
            order.getOrder()
            print(order.order)
            order.allOrders.append(order) #This will add the one instance of order to a list that holds all orders, or at least it will try to.
        elif menu_choice == '2':
            print("All orders placed:")
            for i, ord in enumerate(allOrders, start=1):
                print(f"Order {i}: {ord.order}")            


   




    
if __name__ == "__main__":
    main()



    
