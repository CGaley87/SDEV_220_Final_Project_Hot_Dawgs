class Choice():
    meat_choice = 'burger', 'hotdog', 'side only'

    def __init__(self): 
        
        while True:
            meat_selection = input("Would you like a burger, hotdog or only a side?: ").strip().lower()
            if meat_selection in self.meat_choice:
                self.meat_choice = meat_selection
                break
            else:
                print("Invalid choice, please choose burger, hotdog or side only.")
        


class Hotdog(Choice):
    #Dictionary of prices for specialty dogs and toppings
    PRICES = {
        "base": {"regular": 3.00, "chicago": 4.50, "coney": 4.25},
        "toppings": {
            "ketchup": 0.25, "mustard": 0.25, "relish": 0.40, "onions": 0.30,
             "chili": 1.00, "nacho cheese": 0.75
        }
    }

    def __init__(self, meat_choice: str):
        self.meat_choice = meat_choice
        self.hotdog_type = "regular"
        self.top_choices = []
        self.order = None
        if self.meat_choice == "hotdog":
            self.order = self.get_order()
        
    def get_order(self):
        #Option to choose a specialty style dog    
        specialty = 'chicago', 'coney'
        toppings = set(self.PRICES["toppings"])

        sp_option = input("Would you like a specialty hot dog? Y/N: ").strip().upper()
        if sp_option == 'Y':
            while True:
                sp_choice = input("Please choose Chicago or Coney Dog: ").strip().lower()
                if sp_choice in specialty:
                    self.hotdog_type = sp_choice
                    break
                print("Invalid choice. Please begin again.")

        else:
        #Option to add topping in a custom way instead
            while True:
                top_option = input("Add a topping? Y/N: ").strip().upper()
                if top_option != 'Y':
                    break
                top_selection = input("Please select a topping choice: ").strip().lower()
                if top_selection in toppings:
                    self.top_choices.append(top_selection)
                else:
                    print("Invalid topping choice. Try again.")

        return {"base": self.hotdog_type, "toppings": list(self.top_choices)}
    


    #Calculate base price and topping price using dicitonary
    def calc_total(self) -> float:
        if not self.order:
            return 0.0
        base = self.order["base"] if self.order["base"] in {"chicago","coney"} else "regular"
        base_price = self.PRICES["base"][base]
        top_total = sum(self.PRICES["toppings"][top] for top in self.order["toppings"])
        return (base_price + top_total)
    
    #Summary total of hotdog order using dictionary for reference
    def print_summary(self):
        if not self.order:
            print("No hotdog ordered.")
            return
        total = self.calc_total()
        tops = ", ".join(self.order["toppings"]) if self.order["toppings"] else "no toppings"
        base_ticket = self.order["base"].title()
        print(f"\nHotdog summary:\n Hotdog: {base_ticket}\n Toppings: {tops}\n Total: ${total:.2f}")

class Burger:
    def __init__(self, meat_choice: str):
        return None # Work in progress
    
class SideOnly:
    def __init__(self, meat_choice: str):
        return None # Work in progress


def main():
    orders = [] # empty list to hold objects ordered.

    while True:
        base_choice = Choice() # always ask for each item

        if base_choice.meat_choice == "hotdog":
            item = Hotdog(base_choice.meat_choice)
        elif base_choice.meat_choice == "burger":
            item = Burger(base_choice.meat_choice)
        else: #side only
            item = SideOnly(base_choice.meat_choice)

        orders.append(item)

        repeat = input("would you like to order another item? Y/N): ").strip().upper()
        if repeat != 'Y':
            break
    
    print("\n--- Final Order Summary ---")
    for i, order in enumerate(orders, start=1):
        print(f"\nItem #{i}")
        order.print_summary()

if __name__ == "__main__":
    main()
