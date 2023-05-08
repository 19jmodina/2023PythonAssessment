from tkinter import *
from tkinter import messagebox

class ordering_items:
    """Order Items Object"""
    def __init__(self, name, price, type, quantity=0):
        self.name = name
        self.price = price
        self.type = type
        self.quantity = quantity
    def price_calc(self):
        return self.price * self.quantity
    
class customer:
    """Customer Object"""
    def __init__(self, name, status):
        self.name = name
        self.status = status
    
class ordering_gui:
    """Main GUI class"""
    def __init__(self, parent):
        # Initialise the title frame
        
        self.ordering_items_list = [ordering_items('A', 1.00, 'main'), ordering_items('B', 2.00, 'main'), ordering_items('C', 3.00, 'main')]
        addon_list = [ordering_items('None', 0, 'addon'), ordering_items('Addon A', 0.5, 'addon'), ordering_items('Addon B', 0.75, 'addon'), ordering_items('Addon C', 1.00, 'addon')]
        self.customer_list = []
        
        self.order_var = StringVar()
        self.addon_var = StringVar()
        self.order_var.set(self.ordering_items_list[0].name)
        self.addon_var.set(addon_list[0].name)
        self.title_frame = Frame(parent)
        title_label1 = Label(self.title_frame, text="Welcome to (Company Name inc.)", font=("Arial", 20))
        self.name_entry = Entry(self.title_frame)
        
        title_button = Button(self.title_frame, text="Confirm", command= lambda: self.button_handler(1))
        
        self.title_frame.grid()
        title_label1.grid(padx=35, pady=100)
        self.name_entry.grid()
        title_button.grid()
        
        self.thanks_frame = Frame(parent)
        
        self.thanks_label = Label(self.thanks_frame, text=f'Thank you for choosing (Company Name inc.) !', font=("Arial", 15))
        
        self.thanks_label.grid(padx=100, pady=100)
        
        self.main_frame = Frame(parent)
        self.main_label1 = Label(self.main_frame, text="Hello customer_name")
        main_label2 = Label(self.main_frame, text="Your orders:")
        self.quantity_entry = Entry(self.main_frame, width=2)
        
        order_item_names = []
        addon_item_names = []
        for i in range(len(self.ordering_items_list)):order_item_names.append(self.ordering_items_list[i].name)
        for i in range(len(addon_list)):addon_item_names.append(addon_list[i].name)
        

        order_drop = OptionMenu(self.main_frame, self.order_var, *order_item_names)    
        addon_drop = OptionMenu(self.main_frame, self.addon_var, *addon_item_names)
       
        main_button = Button(self.main_frame, text="Proceed To Checkout", command= lambda: self.button_handler(2))


        self.main_label1.grid()
        main_label2.grid()
        self.quantity_entry.grid()
        order_drop.grid()
        addon_drop.grid()
        main_button.grid()

        self.current_orders = []

        self.checkout1_frame = Frame(parent)
        checkout1_label1 = Label(self.checkout1_frame, text="Checkout")
        checkout1_label2 = Label(self.checkout1_frame, text="Your orders:")
        self.checkout1_quantity_label = Label(self.checkout1_frame, text="Quantity")
        self.checkout1_price_label = Label(self.checkout1_frame, text="Price")
        self.checkout1_orders_label = Label(self.checkout1_frame, text="Orders")
        self.checkout1_addons_label = Label(self.checkout1_frame, text="Addons")
        self.checkout1_total_label = Label(self.checkout1_frame, text="Total")
        checkout1_button1 = Button(self.checkout1_frame, text="Edit Order", command= lambda: self.button_handler(3))
        checkout1_button2 = Button(self.checkout1_frame, text="Confirm Order")

        checkout1_label1.grid()
        checkout1_label2.grid()
        self.checkout1_quantity_label.grid()
        self.checkout1_price_label.grid()
        self.checkout1_orders_label.grid()
        self.checkout1_addons_label.grid()
        self.checkout1_total_label.grid()
        checkout1_button1.grid()
        checkout1_button2.grid()

    def button_handler(self, id):
        #Handle all button commands
        match id:
            case 1:
                """Add delay between switching frames"""
                self.thanks_label.configure(text=f'Thank you for choosing (Company Name inc.) {self.name_entry.get()}!')
                self.main_label1.configure(text=f'Hello {self.name_entry.get()}!')
                self.title_frame.grid_forget()
                self.thanks_frame.grid()
                root.after(2000, self.thanks_frame.grid_forget)
                root.after(2100, self.main_frame.grid)
            case 2:
                for i in range(len(self.ordering_items_list)):
                    if str(self.order_var.get()) == self.ordering_items_list[i].name:
                        self.current_orders.append(self.ordering_items_list[i])
                        self.ordering_items_list[i].quantity += int(self.quantity_entry.get())
                for i in range(len(self.current_orders)):
                    self.checkout1_price_label.configure(text=f'${self.current_orders[i].price}')
                    self.checkout1_quantity_label.configure(text=self.current_orders[i].quantity)
                    self.checkout1_orders_label.configure(text=self.current_orders[i].name)
                    self.checkout1_addons_label.configure(text=self.addon_var.get())
                    self.checkout1_total_label.configure(text=f'${self.current_orders[i].price * self.current_orders[i].quantity}')
                
                self.main_frame.grid_forget()
                self.checkout1_frame.grid()
            case 3: 
                self.checkout1_frame.grid_forget()
                self.main_frame.grid()
            case 4:
                pass

"""Main Routine"""
if __name__ == "__main__":
    root = Tk()
    show_gui = ordering_gui(root)
    root.geometry("500x350")
    root.mainloop()