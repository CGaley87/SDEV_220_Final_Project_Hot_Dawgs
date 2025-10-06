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
        {"Hotdog": 3.00, "Burger": 4.50, "French Fries": 2.00
        },
        "toppings": 
        {
            "Nacho Cheese": 0.50, "American Slice Cheese": 0.50, "Ketchup": 0.25, "Mustard": 0.25,
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
             self.items_ordered.append({"Item:": "Hotdog", "Toppings": itemToppings})



            elif foodChoice == '2' and self.burger:
                itemToppings = self.getToppings()
                self.items_ordered.append({"Item:": "Burger", "Toppings": itemToppings})


            elif foodChoice == '3' and self.fries:
                itemFries = self.getFries()
                self.items_ordered.append({"Items": "French Fries", "Size": itemFries})

            elif foodChoice == '4' and self.drink:
                itemDrink = self.getDrink()
                self.items_ordered.append({"Items": itemDrink})
                
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
            side_choice = int(input("Enter size choice for Fries. "))
            if 1 <= side_choice <= 3:
                size.append(fry_options[side_choice - 1])
                break
            else:
                "Error, please enter 1, 2 or 3"

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


def main():
    allOrders = []
    menu = Menu( hotdog=True, burger=True, fries=True, drink=True)
    while True:    
        #While loop to keep displaying menu until user exits                                     
        menu_choice = display_menu()

        if menu_choice == '1':

            order = Order(menu.hotdog, menu.burger, menu.fries, menu.drink)
            order.getOrder()
            print(order.items_ordered)
            allOrders.append(order) #This will add the one instance of order to a list that holds all orders, or at least it will try to.
        elif menu_choice == '2':
            print("All orders placed:")
            for i, ord in enumerate(allOrders, start=1):
                print(f"\nOrder {i}:")
                for item in ord.items_ordered:
                    if "Toppings" in item:
                        print(f"  {item['Item']} with {', '.join(item['Toppings'])}")
                    elif "Size" in item:
                        print(f"  {item['Item']} ({item['Size']})")


if __name__ == "__main__":
    main()




