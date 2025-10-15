# Curtis Galey, Nathan Schoenike, Isaiah Kerby
#menu.py
#Menu superclass which holds all prices. Moved to its own file to allow it to be called in multiple places.
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
