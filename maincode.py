# Curtis Galey, Nathan Schoenike, Isaiah Kerby
# maincode.py
# This is the maincode of our program. It allows you to cycle through the entire
#  menu and see what the expected outputs are to be. Toppings can be added freely
#  without breaking the system.

from enum import Enum

#enum for picking toppings in getToppings
class FoodToppings(Enum):
    nacho_cheese = 1
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
    chili = 14

#Menu superclass which holds all prices
class Menu():
    PRICES = {
        "base": 
        {"Hotdog": 3.00, "Burger": 4.50, 
         "French Fries": {"Small": 1.50, "Medium": 2.00, "Large": 2.50}
        },
        "toppings": 
        {
            "Nacho Cheese": 0.50, "American Cheese": 0.50, "Ketchup": 0.25, "Mustard": 0.25,
            "Mayo": 0.25, "Lettuce": 0.25, "Tomato": 0.25, "Onion": 0.25, "Pickles": 0.25, "Bacon": 1.00,
            "Mushrooms": 0.25, "Relish": 0.25, "Plain": 0.00, "Chili": 0.75
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

#Order subclass which inherits the prices
class Order(Menu):
    def __init__(self, hotdog, burger, fries, drink):
        super().__init__(hotdog, burger, fries, drink)
        self.items_ordered = []
#getOrder function which just handles which type of base item they order
    def getOrder(self):
        while True:
            print("Choose an option from below (Press 0 to stop order):")
            print ("1. Hotdog")
            print ("2. Burger")
            print ("3. French Fries")
            print ("4. Drink")
            foodChoice = input("Enter your choice: ")

#0 input breaks them out of loop, otherwise each choice corresponds to base item, if toppings are needed the getToppings method obtains them
            if foodChoice == '0':
                break
#self.hotdog can be used to 
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
        #topping list that holds toppings for an item, one element of the array (multiple toppings) corresponds 
        #to only one base item ordered 
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
            print("14. Chili")
            topping_choice = input("Enter topping numbers: (0 to finish) ")
            if topping_choice == '0' and len(toppings) == 0: #This is for if they are done picking toppings and have at least one
                topping_choice = FoodToppings(13)
                toppings.append(topping_choice.name)
                break
            elif topping_choice == '0' and len(toppings) > 0: #This is for if they are done picking toppings and have at least one
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
        #size array to hold the option they choose
        size = []
        fry_options = ["Small", "Medium", "Large"]
        while True:
            print("Small, Medium or Large")
            print("1. Small")
            print("2. Medium")
            print("3. Large")
            
            try:
                size_choice = int(input("Enter size choice for Fries: "))
                if 1 <= size_choice <= 3:
                    size.append(fry_options[size_choice - 1])
                    return fry_options[size_choice - 1]
                else:
                    print("Error, please enter 1, 2 or 3")
            except ValueError:
                print("Error, please enter a number 1, 2 or 3")

    def getDrink(self):
        drink = []
        drink_options = ["Fountain", "Sweet Tea", "Water"]
        while True:
            print("Drink options:")
            print("1. Fountain")
            print("2. Sweet Tea")
            print("3. Water")
            try:

                drink_choice = int(input("Enter drink choice: "))
                if 1 <= drink_choice <= 3:
                    drink.append(drink_options[drink_choice - 1])
                    return drink_options[drink_choice - 1]
                else:
                    print("Error, please enter 1, 2, or 3")
            except ValueError:
                print("Error, please enter a number 1, 2 or 3")

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



#calculates the subtotal from the order
class SubtotalCalculator:
    

    def __init__(self, items):
        self.items = items

    def calculate_subtotal(self):
        #initialize subtotal with 0
        subtotal = 0.0
        for item in self.items:
            if item["Item"] in ["Hotdog", "Burger"]:
                subtotal += Menu.PRICES["base"].get(item["Item"], 0.0)
        
                toppings = item.get("Toppings", [])
                subtotal += sum(Menu.PRICES["toppings"].get(t, 0.0) for t in toppings)
            elif item["Item"] == "French Fries":
                #Default to small size for convinence off cutstomer if there is system error.
                size = item.get("Size", "Small")
                subtotal += Menu.PRICES["base"]["French Fries"].get(size, 0.0)
                
            elif item["Item"] in Menu.PRICES["drinks"]:
                subtotal += Menu.PRICES["drinks"][item['Item']]
            else:   
                print(f"Warning: Unknown item '{item['Item']}' encountered in order.")                                                              

                                                       
        return round(subtotal, 2)
    
    #uses round to represent it as a float so we can correctly add up all the prices
            

                

#calculates the sales tax from a subtotal
class SalesTaxCalculator:
    TAX_RATE = 0.07

    def __init__(self, subtotal):
        self.subtotal = subtotal

    def calculate_tax(self):
        return round(self.subtotal * self.TAX_RATE, 2)
    

#calculates the total from the subtotal and the sales tax
class TotalCalculator:
    def __init__(self, subtotal, tax):
        self.subtotal = subtotal
        self.tax = tax

    def calculate_total(self):
        return round(self.subtotal + self.tax, 2)


#prints a receipt of items purchased, subtotal, tax, and total
class ReceiptPrinter:
    def __init__(self, items, subtotal, tax, total):
        self.items = items
        self.subtotal = subtotal
        self.tax = tax
        self.total = total

#receipt which prints individual orders
    def print_receipt(self):
        print("\n    Hot Dawgs Burger and Hotdog Stand Receipt")
        print("--------------------------------------------")
        
        for item in self.items:
            print(f"{item['Item']}:")
            if "Toppings" in item:
                print("  Toppings: " + ", ".join(item["Toppings"]))
            
            if "Size" in item:
                print(f"  Size: {item['Size']}")
            if "Drink" in item:
                print(f"  Drink: {item['Drink']}")
        print(f"\nSubtotal: ${self.subtotal:.2f}")
        print(f"Sales Tax (7%): ${self.tax:.2f}")
        print(f"Total: ${self.total:.2f}")
        print("--- Thank you and have a great day! ---\n")


def main():
    #Empty list to hold all orders, adds to it as they are made
    #Lists for subtotal and taxes are used to map corresponding elements with the orders, also used to sum earnings which is in menu_choice = 2
    
    allOrders = []
    allSubtotals = []
    allTaxes = []
    menu = Menu( hotdog=True, burger=True, fries=True, drink=True)
    while True:    
        #While loop to keep displaying menu until user exits                                     
        menu_choice = display_menu()

        if menu_choice == '1':
#takes the instance of the order that was just finished after getOrder is called, and passes it through the calculators for pricing
            order = Order(menu.hotdog, menu.burger, menu.fries, menu.drink)
            order.getOrder()
            items = order.items_ordered

            subtotal = SubtotalCalculator(items).calculate_subtotal()
            tax = SalesTaxCalculator(subtotal).calculate_tax()
            total = TotalCalculator(subtotal, tax).calculate_total()
            receipt = ReceiptPrinter(items, subtotal, tax, total)
            receipt.print_receipt()
            allSubtotals.append(subtotal)
            allTaxes.append(tax)
            allOrders.append(order) #This will add the one instance of order to a list that holds all orders
        elif menu_choice == '2':
            total_sales = sum(allSubtotals)
            total_tax = sum(allTaxes)
            
            print(f"\nDaily Sales Report:")
            print(f"Total Sales (before tax): ${total_sales:.2f}")
            print(f"Total Sales Tax Collected: ${total_tax:.2f}\n")
            print("All orders placed:")
            for i, subtotal  in enumerate(allSubtotals, start=1):
                tax = allTaxes[i-1]
                print (f"Order {i} - Subtotal: ${subtotal:.2f}, Tax: ${tax}")

            return 
                
if __name__ == "__main__":
    main()


