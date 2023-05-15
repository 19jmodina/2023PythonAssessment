from tkinter import *
from tkinter import messagebox
import math

class main_items:
    """Order Items Object"""
    def __init__(self, name, price, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def __str__(self): # VERY COOL!!!
        return f'{self.name}'
    def total(self):
        return self.price * self.quantity
class addon_items:
    """Addon Items Object"""
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def __str__(self): # VERY COOL!!!
        return f'{self.name}'

class customer:
    """Customer Object"""
    def __init__(self, name, status):
        self.name = name
        self.status = status

class ordering_gui:
    """Main GUI class"""
    def __init__(self, parent):
        # Initialise the title frame
        self.main_items_list = [main_items('A', 1.00), main_items('B', 2.00), main_items('C', 3.00)]
        self.addon_list = [addon_items('None', 0), addon_items('Addon A', 0.5), addon_items('Addon B', 0.75), addon_items('Addon C', 1.00)]
        self.dictionary_test = {}
        self.count = 0
        self.customer_list = []
        self.order_var0 = StringVar()
        self.addon_var0 = StringVar()
        quantity_var0 = IntVar()
        self.order_var0.set(self.main_items_list[0].name)
        self.addon_var0.set(self.addon_list[0].name)
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
        self.order_wrapper = Frame(self.main_frame)
        self.order_elements = Frame(self.order_wrapper)
        self.main_label1 = Label(self.main_frame, text="Hello customer_name")
        main_label2 = Label(self.main_frame, text="Your orders:")
        
        main_button = Button(self.main_frame, text="Proceed To Checkout", command= lambda: self.button_handler(2))
        self.create_widgets_button = Button(self.main_frame, text="Create Widgets", command= lambda: self.button_handler(4))

        self.create_widgets_button.grid()
        self.order_wrapper.grid()
        self.order_elements.grid()
        self.main_label1.grid()
        main_label2.grid()
        main_button.grid()

        self.current_orders = []
        self.current_addons = []
        self.create_widgets()
        self.checkout1_frame = Frame(parent)
        checkout1_label1 = Label(self.checkout1_frame, text="Checkout")
        checkout1_label2 = Label(self.checkout1_frame, text="Your orders:")
        checkout1_button1 = Button(self.checkout1_frame, text="Edit Order", command= lambda: self.button_handler(3))
        checkout1_button2 = Button(self.checkout1_frame, text="Confirm Order")

        checkout1_label1.grid()
        checkout1_label2.grid()
        checkout1_button1.grid(row=4, column=0)
        checkout1_button2.grid(row=4, column=1)

    def create_widgets(self):
        """Create widgets"""
        frames = []
        widgets = []
        if self.count >= 3:
            self.create_widgets_button['state'] = 'disabled'
        else:
            self.count += 1
            self.dictionary_test[f"self.order_var{self.count}"] = StringVar()
            self.dictionary_test[f"self.addon_var{self.count}"] = StringVar()
            self.dictionary_test[f"quantity_var{self.count}"] = IntVar()
            self.dictionary_test[f"self.addon_var{self.count}"].set(self.addon_list[0].name)
            self.dictionary_test[f"self.order_var{self.count}"].set(self.main_items_list[0].name)
            frame = Frame(self.order_wrapper)
            frames.append(frame)
            qe = Entry(frame, textvariable=self.dictionary_test[f"quantity_var{self.count}"], width=2)
            order_drop = OptionMenu(frame, self.dictionary_test[f"self.order_var{self.count}"], *self.main_items_list)
            addon_drop = OptionMenu(frame, self.dictionary_test[f"self.addon_var{self.count}"], *self.addon_list)
            print(self.dictionary_test)
            widgets.append(qe)
            widgets.append(order_drop)
            widgets.append(addon_drop)
            frame.grid()
            qe.grid(row=0, column=0)
            order_drop.grid(row=0, column=1)
            addon_drop.grid(row=0, column=2)
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
                for i in range(self.count):
                    order_name = self.dictionary_test[f"self.order_var{i+1}"].get()
                    addon_name = self.dictionary_test[f"self.addon_var{i+1}"].get()
                    quantity = self.dictionary_test[f"quantity_var{i+1}"].get()
                    for i in self.main_items_list:
                        if i.name == order_name:
                            i.quantity += quantity
                            self.current_orders.append(i)
                            for i in self.addon_list:
                                if i.name == addon_name:
                                    self.current_addons.append(i)
                        
                print(self.current_orders)
                pricesum = 0
                quantitysum = 0
                order_frame_list = []
                order_wid = []
                for i in range(len(self.current_orders)):
                    print(i)
                    order_frame = Frame(self.checkout1_frame)
                    order_frame_list.append(order_frame)
                    pricesum += self.current_orders[i].price
                    quantitysum += self.current_orders[i].quantity
                    self.checkout1_price_label = Label(order_frame, text=f'${self.current_orders[i].price}')
                    self.checkout1_quantity_label = Label(order_frame, text=f'{self.current_orders[i].quantity}')
                    self.checkout1_orders_label = Label(order_frame, text=self.current_orders[i].name)
                    # self.checkout1_addons_label = Label(order_frame, text=self.current_orders[i].addon)
                    self.checkout1_total_label = Label(order_frame, text=f'${main_items.total(self.current_orders[i])}')
                    order_wid.append(self.checkout1_price_label)
                    order_wid.append(self.checkout1_quantity_label)
                    order_wid.append(self.checkout1_orders_label)
                    # order_wid.append(self.checkout1_addons_label)
                    order_wid.append(self.checkout1_total_label)
                    self.checkout1_price_label.grid(row=0, column=0)
                    self.checkout1_quantity_label.grid(row=0, column=1)
                    self.checkout1_orders_label.grid(row=0, column=2)
                    # self.checkout1_addons_label.grid(row=0, column=3)
                    self.checkout1_total_label.grid(row=0, column=4)
                    order_frame.grid(row=3+i)
                    print(order_wid)

                self.main_frame.grid_forget()
                self.checkout1_frame.grid()
            case 3:
                self.current_orders = []
                order_frame_list = []
                order_wid = []
                for i in range(len(self.main_items_list)):
                    if self.main_items_list[i].quantity > 0:
                        self.main_items_list[i].quantity = 0
                self.checkout1_frame.grid_forget()
                self.main_frame.grid()
            case 4:
                self.create_widgets()
                

"""Main Routine"""
if __name__ == "__main__":
    root = Tk()
    show_gui = ordering_gui(root)
    root.geometry("500x350")
    root.mainloop()