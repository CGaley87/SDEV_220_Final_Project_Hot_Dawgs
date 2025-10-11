# Curtis Galey, Nathan Schoenike, Isaiah Kerby
# gui.py
# This is the tkinter code to create a GUI for our maincode.py. This creates
#  a GUI that allows for selecting food/drink items and outputs a Total after tax.
#  It also adds finalized orders to a Daily Summary for review of the days sales.
#  The current coding allows for the easy addition of toppings in maincode.py without
#  having to overhaul the system.

from maincode import *
import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        #Main window title
        self.title("Hot Dawgs")
        #Main window size by pixel. Can be adjusted larger if desired. Height below 900 cuts off buttons
        self.geometry("800x900")

        #storing lists matching maincode.py
        self.all_orders = []
        self.all_subtotals = []
        self.all_taxes = []

        #Home screen
        ttk.Label(self, text="The Hot Dawgs Menu", font=("Segoe UI", 18, "bold")).pack(pady=16)

        btn_row = ttk.Frame(self)
        btn_row.pack(pady=8)
        ttk.Button(btn_row, text="Start a new order", command=lambda: self.start_order(True)).grid(row=0, column=0, padx=6)
        ttk.Button(btn_row, text="View daily sales report", command=self.show_report).grid(row=0, column=1, padx=6)

        #output frame
        self.output = tk.Text(self, height=20, width=80, state="disabled")
        self.output.pack(pady=12)

    #Initialize ordering
    def start_order(self, fresh: bool = False):
        #reset current_order list
        if fresh or not hasattr(self, "current_order"):
            self.current_order = []
        #Clean window on starting new order
        if fresh:
            self.write("Select an item to add to the order: ")

        #Ensure fresh window starting out
        if hasattr(self,"order_frame") and self.order_frame.winfo_exists():
            self.order_frame.destroy()
        if hasattr(self, "subpanel") and self.subpanel.winfo_exists():
            self.subpanel.destroy()
        
        #create frame for order
        self.order_frame = ttk.Frame(self)
        self.order_frame.pack(pady=10)

        #Buttons for each main group
        ttk.Button(self.order_frame, text="Burger", width=20,
                   command=lambda: self.choose_item("Burger")).grid(row=0, column=0, padx=8, pady=8)
        ttk.Button(self.order_frame, text="Hotdog", width=20,
                   command=lambda: self.choose_item("Hotdog")).grid(row=0, column=1, padx=8, pady=8)
        ttk.Button(self.order_frame, text="French Fries", width=20,
                   command=lambda: self.choose_item("French Fries")).grid(row=1, column=0, padx=8, pady=8)
        ttk.Button(self.order_frame, text="Drink", width=20,
                   command=lambda: self.choose_item("Drink")).grid(row=1, column=1, padx=8, pady=8)

        #Finish order button
        ttk.Button(self.order_frame, text="Finish Order",
                   command=lambda: self._finalize_order()).grid(row=2, column=0, columnspan=2, pady=(12, 0))

        #Manage Items button
        ttk.Button(self.order_frame, text="Manage Items",
                   command=lambda: self.open_manage_items()).grid(row=3, column=0, columnspan=2, pady=(8,0))
        
    def choose_item(self, item_type):
        if item_type in ("Burger", "Hotdog"):
            self.select_toppings_ui(item_type)
        elif item_type == "French Fries":
            self.select_fries_ui()
        elif item_type == "Drink":
            self.select_drink_ui()
        
    def select_toppings_ui(self, item_type:str):
        #code used to take down any previous subpanel. Should be in all subpanel methods
        if hasattr(self,"subpanel") and self.subpanel.winfo_exists():
            self.subpanel.destroy()

        #create panel for toppings
        self.subpanel = ttk.Frame(self)
        self.subpanel.pack(pady=10)

        ttk.Label(self.subpanel,
                  text=f"{item_type} - choose toppings",
                  font=("Arial", 12, "bold")
                  ).grid(row=0, column=0, columnspan=3, pady=(0,8))
        
        #get toppings from maincode.py
        topping_names = list(Menu.PRICES["toppings"].keys())
        #BooleanVar assigned to "Plain" if no toppings selected
        self.toppings_options = {name: tk.BooleanVar(value=(name =="Plain")) for name in topping_names}

        #Create check buttons for each topping
        cols = 3
        for i, name in enumerate(topping_names, start=1):
            row, column = 1 + (i - 1) // cols, (i - 1) % cols
            var = self.toppings_options[name]
            ttk.Checkbutton(self.subpanel,
                            text=name,
                            variable=var,
                            command=lambda n=name: self.on_topping_toggle(n)
                            ).grid(row=row, column=column, sticky="w", padx=6, pady=4)

        #row_after is placing the following buttons after all the checkboxes
        row_after = 1 + (len(topping_names) - 1) // cols + 1
        ttk.Button(self.subpanel, text=f"Add {item_type}",
                   command=lambda: self.add_burger_hotdog(item_type)
                   ).grid(row=row_after, column=0, pady =10)
        #Button created to go back for mistaken choice
        ttk.Button(self.subpanel, text="Back",
                   command=lambda: self.start_order(False)
                   ).grid(row=row_after, column=1, pady=10, sticky="w")
    
    def select_fries_ui(self):
        #code used to take down any previous subpanel. Should be in all subpanel methods
        if hasattr(self, "subpanel") and self.subpanel.winfo_exists():
            self.subpanel.destroy()

        #create subpanl for fries
        self.subpanel = ttk.Frame(self)
        self.subpanel.pack(pady=10)

        ttk.Label(self.subpanel, text="Select French Fry size:",
                  font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=3, pady=(0, 8))
        
        #Get sizes from maincode.py
        sizes = list(Menu.PRICES["base"]["French Fries"].keys())

        #create a radio button selection depending on which Fry size
        self.size_option = tk.StringVar(value="Medium")
        for i, size in enumerate(sizes):
            ttk.Radiobutton(self.subpanel, text=f"{size} - ${Menu.PRICES['base']['French Fries'][size]:.2f}",
                            variable=self.size_option, value=size).grid(row=i+1, column=0, sticky="w", padx=10, pady=4)

        #row_after used to place buttons after radio buttons above
        row_after = len(sizes) + 1
        ttk.Button(self.subpanel, text="Add Fries",
                   command=self.add_fries).grid(row=row_after, column=0, pady=10)
        ttk.Button(self.subpanel, text="Back",
                   command=lambda: self.start_order(False)).grid(row=row_after, column=1, pady=10)
        
    def select_drink_ui(self):
        #code used to take down any previous subpanel. Should be in all subpanel methods
        if hasattr(self, "subpanel") and self.subpanel.winfo_exists():
            self.subpanel.destroy()

        #create drink subpanel
        self.subpanel = ttk.Frame(self)
        self.subpanel.pack(pady=10)

        ttk.Label(self.subpanel, text="Select Drink",
                  font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=3, pady=(0,8))
        
        #Get drink options and prices from maincode.py
        drink_prices = Menu.PRICES["drinks"]
        self.drink_option = tk.StringVar(value=next(iter(drink_prices)))

        #assign radio buttons for drink options
        for i, (name, price) in enumerate(drink_prices.items(), start=1):
            ttk.Radiobutton(
                self.subpanel,
                text=f"{name} - ${price:.2f}",
                variable=self.drink_option,
                value=name
            ).grid(row=i, column=0, sticky="w", padx=10, pady=4)

        #row after code to create buttons after radiobuttons
        row_after = len(drink_prices) + 1
        ttk.Button(self.subpanel, text="Add Drink",
                   command=self.add_drink).grid(row=row_after, column=0, pady=(10,0), sticky="w")
        ttk.Button(self.subpanel, text="Back",
                   command=lambda: self.start_order(False)).grid(row=row_after, column=1, pady=(10,0), sticky="w")

    #Prevent Plain + something else code
    def on_topping_toggle(self, name: str):
        #If plain is selected, this makes sure all others are deselected
        if name == "Plain" and self.toppings_options["Plain"].get():
            for n, var in self.toppings_options.items():
                if n != "Plain":
                    var.set(False)
        #If any other topping is selected, Plain is deselected automatically
        elif name != "Plain" and self.toppings_options[name].get():
            self.toppings_options["Plain"].set(False)

    def add_burger_hotdog(self, item_type: str):
        #Method for adding a burger or hotdog
        #This line build the toppings, checking to see which boxes are ticked
        toppings = [n for n, v in self.toppings_options.items() if v.get()]
        #This assumes Plain if no other option selected
        if not toppings:
            toppings = ["Plain"]
        #This checks to see if there is an existing order. If not, it creates one.
            #This is failsafe to ensure the code doesn't break
        if not hasattr(self, "current_order"):
            self.current_order = []
        #Build the item
        self.current_order.append({"Item": item_type, "Toppings": toppings})
        #refreshes the display
        self.render_order_preview()
        #return to main menu
        self.start_order(False)

    def add_fries(self):
        #built same as add_burger_hotdog
        size = self.size_option.get()
        if not hasattr(self, "current_order"):
            self.current_order = []
        self.current_order.append({"Item": "French Fries", "Size": size})
        self.render_order_preview()
        self.start_order(False)

    def add_drink(self):
        #built same as add_burger_hotdog
        choice = self.drink_option.get()
        if not hasattr(self, "current_order"):
            self.current_order = []
        self.current_order.append({"Item": "Drink", "Drink": choice})
        self.render_order_preview()
        self.start_order(False)

    def line_price(self, item) -> float:
        #Price calucaltions
        #Burger and Hotdog + toppings
        if item["Item"] in ("Burger", "Hotdog"):
            base = Menu.PRICES["base"][item["Item"]]
            tops = item.get("Toppings", [])
            tops_sum = sum(Menu.PRICES["toppings"].get(t, 0.0) for t in tops)
            return round(base + tops_sum, 2)
        
        #Fries price
        if item["Item"] == "French Fries":
            size = item.get("Size", "Small")
            return round(Menu.PRICES["base"]["French Fries"].get(size, 0.0), 2)
        
        #Drink price
        if item["Item"] == "Drink":
            drink_name = item.get("Drink", "")
            return round(Menu.PRICES["drinks"].get(drink_name, 0.0), 2)
        
        return 0.0

    def render_order_preview(self):
        #This is the method to build the text displayed.
        if not hasattr(self,"current_order"):
            return
        #Initialize subtotal
        lines = ["Current order:"]
        subtotal = 0.0

        #loops through every item in the order to create it all in the text box
        for it in self.current_order:
            price = self.line_price(it)
            subtotal += price

            if it["Item"] in ("Burger", "Hotdog"):
                tops = ", ".join(it.get("Toppings", [])) or "Plain"
                lines.append(f"- {it['Item']}: ({tops}) .... ${price:.2f}")
            elif it["Item"] == "French Fries":
                lines.append(f"- Fries: {it.get('Size', 'Small')} .... ${price:.2f}")
            elif it["Item"] == "Drink":
                lines.append(f"- Drink: {it.get('Drink', '')} .... ${price:.2f}")
            #This line is future proofing incase an item is added outside of the above parameters
            else:
                lines.append(f"- {it["Item"]} .... ${price}:.2f")
        
        tax = SalesTaxCalculator(subtotal).calculate_tax()
        total = TotalCalculator(subtotal, tax).calculate_total()

        lines += [
            "-" * 32,
            f"Subtotal: ${subtotal:.2f}",
            f"Tax (7%): ${tax:.2f}",
            f"Total:    ${total:.2f}"
        ]
        #writes it all into the text box
        self.write("\n".join(lines))

    def open_manage_items(self):
        #This method allows for the deletion of items that may no longer be desired
        if not getattr(self, "current_order", None):
            self.write("Not items to manage.")
            return
        
        #build manager
        self.mgr = tk.Toplevel(self)
        self.mgr.title("Manage Items")
        self.mgr.transient(self) #this is used to keep it on top

        label = ttk.Label(self.mgr, text="Select item(s) to delete:")
        label.grid(row=0, column=0, padx=10, pady=(10, 4), sticky="w")


        #listbox showing ordered items
        self.mgr_list = tk.Listbox(self.mgr, selectmode="extended", width=60, height=8)
        self.mgr_list.grid(row=1, column=0, padx=10, pady=4)

        #fill listbox
        for label in self.order_labels():
            self.mgr_list.insert("end", label)
        
        #create new frame and buttons for manager
        btns = ttk.Frame(self.mgr)
        btns.grid(row=2, column=0, padx=10, sticky="e")
        ttk.Button(btns, text="Delete Selected", command=self.delete_selected_items).grid(row=0, column=0, padx=(0,6))
        ttk.Button(btns, text="Close", command=self.mgr.destroy).grid(row=0, column=1)

    def order_labels(self):
        #This is to create readable labels for self.current_order
        labels = []
        for it in getattr(self, "current_order", []):
            if it["Item"] in ("Burger", "Hotdog"):
                tops = ", ".join(it.get("Toppings", [])) or "Plain"
                labels.append(f"{it['Item']} ({tops})")
            elif it["Item"] == "French Fries":
                labels.append(f"Fries ({it.get('Size', 'Small')})")
            elif it["Item"] == "Drink":
                labels.append(f"Drink ({it.get('Drink','')})")
            else:
                labels.append(it["Item"])
        return labels

    def delete_selected_items(self):
        #method to delete selected items
        sel = list(self.mgr_list.curselection())
        if not sel:
            return
        for idx in reversed(sel):
            del self.current_order[idx]

        self.render_order_preview()

        self.mgr_list.delete(0, "end")
        if not self.current_order:
            self.mgr.destroy()
            self.start_order(fresh=False)
            return
        for label in self.order_labels():
            self.mgr_list.insert("end", label)
    
    def show_report(self):
        #Method to show the daily summary
        total_sales = sum(self.all_subtotals)
        total_tax = sum(self.all_taxes)
        lines = [
            "Daily Sales Report:",
            f"Total Sales (before tax): ${total_sales:.2f}",
            f"Total Sales Tax Collected: ${total_tax:.2f}",
            f"Orders placed: {len(self.all_subtotals)}",
        ]
        self.write("\n".join(lines))

    def _finalize_order(self):
        #Method to finalize an order and commit it to the daily summary
        if not getattr(self, "current_order", None):
            self.write("No items in order yet.")
            return
        
        subtotal = sum(self.line_price(it) for it in self.current_order)
        tax = SalesTaxCalculator(subtotal).calculate_tax()
        total = TotalCalculator(subtotal, tax).calculate_total()

        #add to running daily totals
        self.all_subtotals.append(subtotal)
        self.all_taxes.append(tax)

        #show final recepit
        lines = ["Receipt:"]
        for it in self.current_order:
            price = self.line_price(it)
            if it["Item"] in ("Burger", "Hotdog"):
                tops = ", ".join(it.get("Toppings", [])) or "Plain"
                lines.append(f"- {it['Item']}: ({tops}) .... ${price:.2f}")
            elif it["Item"] == "French Fries":
                lines.append(f"- Fries: {it.get('Size', 'Small')} .... ${price:.2f}")
            elif it["Item"] == "Drink":
                lines.append(f"- Drink: {it.get('Drink', '')}) .... ${price:.2f}")
            else:
                lines.append(f"- {it["Item"]} .... ${price}.2f")
        lines += [
            "-" * 32,
            f"Subtotal: ${subtotal:.2f}",
            f"Tax (7%): ${tax:.2f}",
            f"Total:    ${total:.2f}"
        ]
        self.write("\n".join(lines))

        #clear and reset for next order
        self.current_order = []

    def write(self, msg: str):
        #Used across GUI to write text
        self.output.configure(state="normal")
        self.output.delete("1.0", "end")
        self.output.insert("end", msg + "\n")
        self.output.configure(state="disabled")

if __name__ == "__main__":
    App().mainloop()
