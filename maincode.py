from enum import Enum

class FoodToppings(Enum):
    cheddar = 1
    swiss = 2
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
        {"Hotdog": 3.00, "Burger": 4.50, 
         "French Fries": {"Small": 1.50, "Medium": 2.00, "Large": 2.50}
        },
        "toppings": 
        {
            "Cheddar Cheese": 0.50, "Swiss Cheese": 0.50, "Ketchup": 0.25, "Mustard": 0.25,
            "Mayo": 0.25, "Lettuce": 0.25, "Tomato": 0.25, "Onion": 0.25, "Pickles": 0.25, "Bacon": 1.00,
            "Mushrooms": 0.25, "Relish": 0.25, "Plain": 0.00
        },
        "drinks":
        {
            "Fountain": 2.00, "Sweet Tea": 2.00, "Water": 0.50
        }
    }
    def __init__(self, hotdog, burger, fries, drink):
        self.hotdog = hotdog
        self.burger = burger
        self.fries = fries
        self.drink = drink

class Order(Menu):
    def __init__(self, hotdog, burger, fries, drink):
        super().__init__(hotdog, burger, fries, drink)
        self.items_ordered = []

    def getOrder(self):
        while True:
            print("Choose an option from below (Press 0 to stop order):")
            print ("1. Hotdog")
            print ("2. Burger")
            print ("3. French Fries")
            print ("4. Drink")
            foodChoice = input("Enter your choice: ")
            if foodChoice == '0':
                break

            elif foodChoice == '1' and self.hotdog:
             itemToppings = self.getToppings()
             self.items_ordered.append({"Item": "Hotdog", "Toppings": itemToppings})



            elif foodChoice == '2' and self.burger:
                itemToppings = self.getToppings()
                self.items_ordered.append({"Item": "Burger", "Toppings": itemToppings})


            elif foodChoice == '3' and self.fries:
                itemFries = self.getFries()
                self.items_ordered.append({"Item": "French Fries", "Size": itemFries})

            elif foodChoice == '4' and self.drink:
                itemDrink = self.getDrink()
                self.items_ordered.append({"Item": itemDrink})
                
            else:
                print("Invalid choice or option not available.")


    def getToppings(self):
        toppings = []
        while True:
            print("Toppings available: (Enter 13 for plain)")
            print("1. Nacho Cheese")
            print("2. American Slice Cheese")
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

    def getFries(self):
        size = []
        fry_options = ["Small", "Medium", "Large"]
        while True:
            print("Small, Medium or Large")
            print("1. Small")
            print("2. Medium")
            print("3. Large")
            
            try:
                size_choice = int(input("Enter size choice for Fries. "))
                if 1 <= size_choice <= 3:
                    size.append(fry_options[size_choice - 1])
                    return fry_options[size_choice - 1]
                else:
                    print("Error, please enter 1, 2 or 3")
            except ValueError:
                print("Error, please enter a number 1, 2 or 3")
            # if 1 <= size_choice <= 3:
            #     size.append(fry_options[size_choice - 1])
            #     break
            # else:
            #     "Error, please enter 1, 2 or 3"

    def getDrink(self):
        drink = []
        drink_options = ["Fountain", "Sweet Tea", "Water"]
        while True:
            for item in enumerate(drink_options):
                print()
            drink_choice = int(input("Enter drink choice"))
            if 1 <= drink_choice <= 3:
                drink.append(drink_options[drink_choice - 1])
                break
            else:
                "Error, please enter 1, 2, or 3"

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
# Below are Sales classes to be added to Final Project burger.py file as of 2025-10-06


# calculate a subtotal from an order.
class SubtotalCalculator:
    

    def __init__(self, items):
        self.items = items

    def calculate_subtotal(self):
        subtotal = 0.0
        for item in self.items_ordered:
            base_price = Menu.PRICES["base"].get(item["Item"], 0.0)
        
            toppings = item.get("Toppings", [])
            topping_cost = sum(Menu.PRICES["toppings"].get(t, 0.0) for t in toppings)

            drink_cost = Menu.PRICES["drinks"].get(item["Item"], 0.0)

            if item["Item"] == "French Fries":
                #Default to small size for convinence off cutstomer if there is system error.
                size = item.get("Size", "Small")
                base_price = Menu.PRICES["base"]["French Fries"].get(size, 0.0)
            subtotal += base_price + topping_cost + drink_cost
        return round(subtotal, 2)
    
    #uses round to represent it as a float so we can correctly add up all the prices
            

                

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
    def __init__(self, items_ordered, subtotal, tax, total):
        self.items_ordered = items_ordered
        self.subtotal = subtotal
        self.tax = tax
        self.total = total

    def print_receipt(self):
        print("\n    Hot Dawgs Burger and Hotdog Stand\n")
        print("\n--- Receipt ---")
        for item in self.items_ordered:
            print(f"{item['Item']}:")
            if item["Toppings"]:
                print("  Toppings: " + ", ".join(item["Toppings"]))
            else:
                print("  Toppings: None")
        print(f"\nSubtotal: ${self.subtotal:.2f}")
        print(f"Sales Tax (7%): ${self.tax:.2f}")
        print(f"Total: ${self.total:.2f}")
        print("--- Thank you and have a great day! ---\n")


def main():
    #Empty list to hold all orders, adds to it as they are made
    print("working")
    allOrders = []
    menu = Menu( hotdog=True, burger=True, fries=True, drink=True)
    while True:    
        #While loop to keep displaying menu until user exits                                     
        menu_choice = display_menu()

        if menu_choice == '1':

            order = Order(menu.hotdog, menu.burger, menu.fries, menu.drink)
            order.getOrder()
            print(order.items_ordered)
            subtot_calc = SubtotalCalculator(order.items_ordered)
            allOrders.append(order) #This will add the one instance of order to a list that holds all orders, or at least it will try to.
        elif menu_choice == '2':
            print("All orders placed:")
            for i, ord in enumerate(allOrders, start=1):
                print(f"\nOrder {i}:")
                subtotal = SubtotalCalculator(ord.items_ordered).calculate_subtotal()
                tax = SalesTaxCalculator(subtotal).calculate_tax()
                total = TotalCalculator(subtotal, tax).calculate_total()

                receipt = ReceiptPrinter(ord.items_ordered, subtotal, tax, total)
                receipt.print_receipt()
                # for item in ord.items_ordered:
                #     if "Toppings" in item:
                #         print(f"  {item['Item']} with {', '.join(item['Toppings'])}")
                #     elif "Size" in item:
                #         print(f"  {item['Item']} ({item['Size']})")
                    



if __name__ == "__main__":
    main()




