from tkinter import *
from tkinter import messagebox


class main_items:
    """Order Items Object"""
    def __init__(self, name, price, quantity=0, addons=None):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.addons = addons
        
    def __str__(self): # VERY COOL!!!
        return f'{self.name}: ${self.price:.2f}'
    def total(self):
        addon_price = 0 # If there are no addons, addon_price will be 0
        if self.addons:
            addon_price = self.addons.price
        return self.quantity * self.price +  self.quantity * addon_price

class addon_items:
    """Addon Items Object"""
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def __str__(self):
        return f'{self.name}: ${self.price:.2f}'

class customer:
    """Customer Object"""
    def __init__(self, name, status):
        self.name = name
        self.status = status

class ordering_gui:
    """Main GUI class"""
    def __init__(self, parent):
        """Initialise GUI"""
        # Initialise the title frame
        self.main_items_list = [main_items('Angus Beef Burger', 1.00), main_items('Burger Queen Wooper', 2.00), main_items('Chik Fil B', 3.00)]
        self.addon_list = [addon_items('None', 0), addon_items('Extra Pickles', 0.50), addon_items('Extra Tears', 0.75), addon_items('Vegan', 100.00)]
        self.dynamic_vars = {}
        self.count = 0
        self.customer_list = []
        self.frames = []
        self.widgets = []
        BTN_WIDTH = 20
        BTN_HEIGHT = 1
        DROP_WIDTH = 30

        self.title_frame = Frame(parent)
        title_label1 = Label(self.title_frame, text="Welcome to (Company Name inc.)", font=("Arial", 20))
        self.name_entry = Entry(self.title_frame)
        
        title_button = Button(self.title_frame, text="Confirm", width=BTN_WIDTH, height=BTN_HEIGHT, command= lambda: self.button_handler(1))
        
        self.title_frame.grid()
        title_label1.grid(padx=35, pady=100)
        self.name_entry.grid()
        title_button.grid()
        
        self.thanks_frame = Frame(parent)
        
        self.thanks_label = Label(self.thanks_frame, text=f'Thank you for choosing (Company Name inc.) !', font=("Arial", 15))
        
        self.thanks_label.grid(padx=100, pady=100)
        
        self.main_frame = Frame(parent)
        self.order_wrapper = Frame(self.main_frame, bg='green')
        self.button_frame = Frame(self.main_frame )

        self.main_label1 = Label(self.main_frame, text="Hello customer_name", bg='yellow', anchor='w', width=68, height=2)
        main_label2 = Label(self.main_frame, text="Your orders:", bg='red', width=68, height=3)
        
        main_button = Button(self.main_frame, width=BTN_WIDTH, height=BTN_HEIGHT, text="Proceed To Checkout", command= lambda: self.button_handler(2))
        self.destroy_widgets_button = Button(self.button_frame, text="-", width=1, borderwidth=2, command= lambda: self.button_handler(5))
        self.create_widgets_button = Button(self.button_frame, text="+", width=1, borderwidth=2, command= lambda: self.button_handler(4))

        
        self.main_label1.grid(row=0, column=0, sticky=EW)
        main_label2.grid(row=1, column=0, sticky=EW)
        self.order_wrapper.grid()
        self.button_frame.grid()
        self.create_widgets()
        self.destroy_widgets_button.grid(row=0, column=0, padx=10)
        self.create_widgets_button.grid(row=0, column=1)
        
        
        main_button.grid()
        
        self.current_orders = []
        
        self.chkout_frame = Frame(parent, bg='pink', width=100)
        self.chk_lower = Frame(self.chkout_frame)
        self.chk1 = Frame(self.chkout_frame)
        self.chk2 = Frame(self.chk1)
        chkout_label1 = Label(self.chk1, text="Checkout", width=70)
        chkout_label2 = Label(self.chk1, text="Your orders:")
        chkout_button1 = Button(self.chk_lower, width=BTN_WIDTH, height=BTN_HEIGHT, text="Edit Order", command= lambda: self.button_handler(3))
        chkout_button2 = Button(self.chk_lower, width=BTN_WIDTH, height=BTN_HEIGHT, text="Confirm Order")

        chkout_label1.grid()
        chkout_label2.grid()
        self.chk1.grid()
        self.chk2.grid()
        chkout_button1.grid(row=4, column=0)
        chkout_button2.grid(row=4, column=1)

        


        
    def callback(self, P):
        if str.isdigit(P) or P == "":
            return True
        else:
            return False
            
    def create_widgets(self):
        """Create widgets"""
        if self.count >= 3:
            self.create_widgets_button['state'] = 'disabled'
            self.destroy_widgets_button['state'] = 'normal'
            messagebox.showinfo(message="You have reached the maximum number of orders")
        else:
            self.destroy_widgets_button['state'] = 'normal' 
            self.count += 1
            self.dynamic_vars[f"self.order_var{self.count}"] = StringVar()
            self.dynamic_vars[f"self.addon_var{self.count}"] = StringVar()
            self.dynamic_vars[f"quantity_var{self.count}"] = IntVar()
            self.dynamic_vars[f"self.addon_var{self.count}"].set(str(self.addon_list[0]))
            self.dynamic_vars[f"self.order_var{self.count}"].set(str(self.main_items_list[0]))
            frame = Frame(self.order_wrapper)
            self.frames.append(frame)
            vcmd = (frame.register(self.callback), '%P')
            qe = Entry(frame, textvariable=self.dynamic_vars[f"quantity_var{self.count}"], width=3, validate='key', validatecommand=(vcmd))
            order_drop = OptionMenu(frame, self.dynamic_vars[f"self.order_var{self.count}"], *self.main_items_list)
            addon_drop = OptionMenu(frame, self.dynamic_vars[f"self.addon_var{self.count}"], *self.addon_list)
        #   print(self.dynamic_vars)
            self.widgets.append(qe)
            self.widgets.append(order_drop)
            self.widgets.append(addon_drop)
            frame.grid(sticky=EW, column=2, padx=90)
            qe.grid(row=0, column=0)
            order_drop.config(width=25)
            addon_drop.config(width=15)
            order_drop.grid(row=0, column=1, pady=2)
            addon_drop.grid(row=0, column=2)

    def remove_widgets(self):
        if self.count <= 1:
            self.destroy_widgets_button['state'] = 'disabled'
            self.create_widgets_button['state'] = 'normal'
            messagebox.showwarning(message="You can't remove any more items, You must have at least one item in your order")
        else:
            if self.frames:
                self.create_widgets_button['state'] = 'normal'
                frame = self.frames.pop()
                frame.destroy()
                self.count -= 1

    def checkout_labels(self):
        self.ord_frames = []
        self.ord_wid = []
        for i in range(len(self.current_orders)):
            # print(i)
            order_frame = Frame(self.chk2, width=80, bg='blue', padx=50)
            self.ord_frames.append(order_frame)
            self.chkout_price_label = Label(order_frame, text=f'${self.current_orders[i].price}', width=3)
            self.chkout_quantity_label = Label(order_frame, text=f'{self.current_orders[i].quantity}', width=3)
            self.chkout_orders_label = Label(order_frame, text=self.current_orders[i].name, width=18)
            self.chkout_addons_label = Label(order_frame, text=self.current_orders[i].addons.name, width=10)
            self.chkout_total_label = Label(order_frame, text=f'${main_items.total(self.current_orders[i])}', width=5)
            self.ord_wid.append(self.chkout_price_label)
            self.ord_wid.append(self.chkout_quantity_label)
            self.ord_wid.append(self.chkout_orders_label)
            self.ord_wid.append(self.chkout_addons_label)
            self.ord_wid.append(self.chkout_total_label)
            self.chkout_price_label.grid(row=0, column=0)
            self.chkout_quantity_label.grid(row=0, column=1)
            self.chkout_orders_label.grid(row=0, column=2)
            self.chkout_addons_label.grid(row=0, column=3)
            self.chkout_total_label.grid(row=0, column=4)
            self.ord_frames[i].grid()
            print(self.ord_wid)

    def button_handler(self, id):
        #Handle all button commands
        match id:
            case 1:
                """Add delay between switching frames"""
                self.thanks_label.configure(text=f'Thank you for choosing (Company Name inc.) {self.name_entry.get()}!')
                self.main_label1.configure(text=f'Hello {self.name_entry.get()}!')
                self.title_frame.grid_forget()
                self.thanks_frame.grid()
                #root.after(2000, self.thanks_frame.grid_forget)
                #root.after(2100, self.main_frame.grid)
                self.thanks_frame.grid_forget()
                self.main_frame.grid()
            case 2:
                """Checkout Logic"""
                for i in range(self.count):
                    order_name = self.dynamic_vars[f"self.order_var{i+1}"].get()
                    addon_name = self.dynamic_vars[f"self.addon_var{i+1}"].get()
                    quantity = self.dynamic_vars[f"quantity_var{i+1}"].get()
                    for item in self.main_items_list:
                        if str(item) == order_name:
                            item.quantity += quantity
                            self.current_orders.append(item)
                            for addon in self.addon_list:
                                if str(addon) == addon_name:
                                    item.addons = addon
                                    print(item)
                                    print(item.addons, 'HELLo')

                # print(self.current_orders)
                
                self.checkout_labels()
                self.chk_lower.grid()
                self.main_frame.grid_forget()
                self.chkout_frame.grid(sticky=EW)
            case 3:
                self.current_orders = []
                self.current_addons = []
                for i in self.ord_frames:
                    i.destroy()
                for i in self.ord_wid:
                    i.destroy()
                print(self.current_orders)
                for i in range(len(self.main_items_list)):
                    if self.main_items_list[i].quantity > 0:
                        self.main_items_list[i].quantity = 0
                self.chkout_frame.grid_forget()
                self.main_frame.grid()
            case 4:
                self.create_widgets()
            case 5:
                self.remove_widgets()
            

"""Main Routine"""
if __name__ == "__main__":
    root = Tk()
    show_gui = ordering_gui(root)
    root.geometry("500x350")
    root.mainloop()