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



    