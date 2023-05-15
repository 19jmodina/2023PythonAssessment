from tkinter import *
from tkinter import messagebox
import math

class ordering_items:
    """Order Items Object"""
    def __init__(self, name, price, type, quantity=0):
        self.name = name
        self.price = price
        self.type = type
        self.quantity = quantity
        
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
        self.ordering_items_list = [ordering_items('A', 1.00, 'main'), ordering_items('B', 2.00, 'main'), ordering_items('C', 3.00, 'main')]
        self.addon_list = [ordering_items('None', 0, 'addon'), ordering_items('Addon A', 0.5, 'addon'), ordering_items('Addon B', 0.75, 'addon'), ordering_items('Addon C', 1.00, 'addon')]
        self.dictionary_test = {}
        self.count = 0
        self.customer_list = []
        self.order_var0 = StringVar()
        self.addon_var0 = StringVar()
        quantity_var0 = IntVar()
        self.order_var0.set(self.ordering_items_list[0].name)
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
        self.count += 1
        self.dictionary_test[f"self.order_var{self.count}"] = StringVar()
        self.dictionary_test[f"self.addon_var{self.count}"] = StringVar()
        self.dictionary_test[f"quantity_var{self.count}"] = IntVar()
        frame = Frame(self.order_wrapper)
        qe = Entry(frame, textvariable=self.dictionary_test[f"quantity_var{self.count}"], width=2)
        order_drop = OptionMenu(frame, self.dictionary_test[f"self.order_var{self.count}"], *self.ordering_items_list)   
        addon_drop = OptionMenu(frame, self.dictionary_test[f"self.addon_var{self.count}"], *self.addon_list)
        frame.grid()
        qe.grid(row=0, column=0)
        order_drop.grid(row=0, column=1)
        addon_drop.grid(row=0, column=2)
        self.checkout1_frame = Frame(parent)
        checkout1_label1 = Label(self.checkout1_frame, text="Checkout")
        checkout1_label2 = Label(self.checkout1_frame, text="Your orders:")
        checkout1_button1 = Button(self.checkout1_frame, text="Edit Order", command= lambda: self.button_handler(3))
        checkout1_button2 = Button(self.checkout1_frame, text="Confirm Order")

        checkout1_label1.grid()
        checkout1_label2.grid()
        checkout1_button1.grid(row=4, column=0)
        checkout1_button2.grid(row=4, column=1)

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
                x=0
                for i in range(len(self.ordering_items_list)):
                    # if str(self.order_var.get()) == self.ordering_items_list[i].name:
                    #     self.current_orders.append(self.ordering_items_list[i])
                    #     self.ordering_items_list[i].quantity += int(self.quantity_entry.get())
                    #     print(str(self.dictionary_test[f"self.order_var{self.count}"]))
                    
                    if str(self.dictionary_test[f"self.order_var{self.count}"].get()) == self.ordering_items_list[i].name:
                        self.current_orders.append(self.ordering_items_list[i])
                        print(self.count)
                        self.ordering_items_list[i].quantity += int(self.dictionary_test[f"quantity_var{self.count}"].get())
                        x += 1
                pricesum = 0
                quantitysum = 0
                order_frame_list = []
                order_wid = []
                for i in range(len(self.current_orders)): 
                    order_frame = Frame(self.checkout1_frame)
                    order_frame_list.append(order_frame)
                    pricesum += self.current_orders[i].price
                    quantitysum += self.current_orders[i].quantity
                    self.checkout1_price_label = Label(order_frame, text=f'${self.current_orders[i].price}')
                    self.checkout1_quantity_label = Label(order_frame, text=f'{self.current_orders[i].quantity}')
                    self.checkout1_orders_label = Label(order_frame, text=self.current_orders[i].name)
                    self.checkout1_addons_label = Label(order_frame, text=self.addon_var0.get())
                    self.checkout1_total_label = Label(order_frame, text=f'${pricesum * quantitysum}')
                    order_wid.append(self.checkout1_price_label)
                    order_wid.append(self.checkout1_quantity_label)
                    order_wid.append(self.checkout1_orders_label)
                    order_wid.append(self.checkout1_addons_label)
                    order_wid.append(self.checkout1_total_label)
                    self.checkout1_price_label.grid(row=0, column=0)
                    self.checkout1_quantity_label.grid(row=0, column=1)
                    self.checkout1_orders_label.grid(row=0, column=2)
                    self.checkout1_addons_label.grid(row=0, column=3)
                    self.checkout1_total_label.grid(row=0, column=4)
                    order_frame.grid(row=3)

                self.main_frame.grid_forget()
                self.checkout1_frame.grid()
            case 3:
                self.current_orders = []
                order_frame_list = []
                order_wid = []
                for i in range(len(self.ordering_items_list)):
                    if self.ordering_items_list[i].quantity > 0:
                        self.ordering_items_list[i].quantity = 0
                self.checkout1_frame.grid_forget()
                self.main_frame.grid()
            case 4:
                """Create widgets"""
                frames = []
                widgets = []
                self.dictionary_test = {}
                if self.count >= 3:
                    self.create_widgets_button['state'] = 'disabled'
                else:
                    self.count += 1
                    self.dictionary_test[f"self.order_var{self.count}"] = StringVar()
                    self.dictionary_test[f"self.addon_var{self.count}"] = StringVar()
                    self.dictionary_test[f"quantity_var{self.count}"] = IntVar()
                    frame = Frame(self.order_wrapper)
                    frames.append(frame)
                    qe = Entry(frame, textvariable=self.dictionary_test[f"quantity_var{self.count}"], width=2)
                    order_drop = OptionMenu(frame, self.dictionary_test[f"self.order_var{self.count}"], *self.ordering_items_list)   
                    addon_drop = OptionMenu(frame, self.dictionary_test[f"self.addon_var{self.count}"], *self.addon_list)
                    widgets.append(qe)
                    widgets.append(order_drop)
                    widgets.append(addon_drop)
                    frame.grid()
                    qe.grid(row=0, column=0)
                    order_drop.grid(row=0, column=1)
                    addon_drop.grid(row=0, column=2)
                


"""Main Routine"""
if __name__ == "__main__":
    root = Tk()
    show_gui = ordering_gui(root)
    root.geometry("500x350")
    root.mainloop()