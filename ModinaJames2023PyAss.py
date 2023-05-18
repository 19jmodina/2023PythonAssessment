"""
James' Burger Bar Ordering System. v 0.9.0
Reorgranised code to make it more readable and easier to debug.
Ran through PeP8 checker.
"""
from tkinter import *
from tkinter import messagebox
import copy


class MainItems:
    """Order Items Object."""

    def __init__(self, name, price, quantity=0, addons=None):
        """Initialise MainItems object."""
        self.name = name
        self.price = price
        self.quantity = quantity
        self.addons = addons

    def __str__(self):
        """Return string + price of main_item object."""
        return f'{self.name}: ${self.price:.2f}'

    def total(self):
        """Calculate total price of individual orders."""
        addon_price = 0
        if self.addons:
            addon_price = self.addons.price
        self.order_total = self.quantity * self.price + self.quantity * addon_price
        return self.order_total


class AddonItems:
    """Addon Items Object."""

    def __init__(self, name, price):
        """Initialise AddonItems object."""
        self.name = name
        self.price = price

    def __str__(self):
        """Return string + price of addon_item object."""
        return f'{self.name}: ${self.price:.2f}'


class Customer:
    """Customer Object."""

    def __init__(self, name, status, sum, pnum=None, order=None):
        """Initialise Customer object."""
        self.name = name
        self.status = status
        self.sum = sum
        self.pnum = pnum
        self.order = []


class OrderingGUI:
    """Main GUI class."""

    def __init__(self, parent):
        """Initialise GUI."""
        self.MainItems_list = [MainItems('Angus Beef Burger', 1.00), MainItems('Burger Queen Wooper', 2.00), MainItems('Chik Fil B', 3.00)]
        self.addon_list = [AddonItems('None', 0), AddonItems('Extra Pickles', 0.50), AddonItems('Extra Tears', 0.75), AddonItems('Vegan', 100.00)]
        self.dynamic_vars = {}
        self.count = 0
        self.frames = []
        self.widgets = []
        self.current_orders = []
        self.name_var = StringVar()
        self.name_var.set('Enter name')
        self.status_var = StringVar()
        self.status_var.set('*')

        self.MAX_WIDGETS = 3
        self.MIN_WIDGETS = 1    
        BTN_WIDTH = 20
        BTN_HEIGHT = 1
        self.PRICE_WIDTH = 6
        self.QUANTITY_WIDTH = 6
        self.NAME_WIDTH = 18
        self.ADDON_WIDTH = 10
        self.TOTAL_WIDTH = 5

        # Title Frame
        self.title_frame = Frame(parent)
        title_label1 = Label(self.title_frame, text="Welcome to the Burger Bar", font=("Arial", 20), bg='peach puff', height=6, width=31)
        self.name_entry = Entry(self.title_frame, textvariable=self.name_var)
        self.name_entry.bind("<FocusIn>", lambda event: self.name_entry.delete(0, END))
        title_button = Button(self.title_frame, text="Confirm", width=BTN_WIDTH, height=BTN_HEIGHT, command=lambda: self.button_handler(1))

        # Thanks Frame
        self.thanks_frame = Frame(parent)
        self.thanks_label = Label(self.thanks_frame, text=f'Thank you for choosing Burger Bar!', font=("Arial", 15), width=45, height=13)
        self.thanks_label.grid()

        # Main Frame
        self.main_frame = Frame(parent)
        self.order_wrapper = Frame(self.main_frame, bg='green')
        self.button_frame = Frame(self.main_frame, bg='peach puff', height=30)
        self.main_label1 = Label(self.main_frame, text="Hello, customer_name", bg='yellow', anchor='w', width=68, height=2)
        main_label2 = Label(self.main_frame, text="Your orders:", bg='red', width=63, height=3)
        main_button = Button(self.main_frame, width=BTN_WIDTH, height=BTN_HEIGHT, text="Proceed To Checkout", command=lambda: self.button_handler(2))
        self.destroy_widgets_button = Button(self.button_frame, text="-", width=1, borderwidth=2, command=lambda: self.button_handler(5))
        self.create_widgets_button = Button(self.button_frame, text="+", width=1, borderwidth=2, command=lambda: self.button_handler(4))

        # Checkout Frames
        self.chkout_frame = Frame(parent, width=100)
        self.chk_lower = Frame(self.chkout_frame)
        self.chk_lower2 = Frame(self.chkout_frame)
        self.chk1 = Frame(self.chkout_frame)
        self.chk2 = Frame(self.chk1)
        chkout_label1 = Label(self.chk1, text="Checkout", width=70, height=2, bg='pink')
        chkout_label2 = Label(self.chk1, text="Your orders:", width=70, height=3, bg='pink')
        self.header = Frame(self.chk2, width=80, padx=50)
        Label(self.header, text='Price', width=self.PRICE_WIDTH, bg='orange').grid(row=0, column=0)
        Label(self.header, text='Quantity', width=self.QUANTITY_WIDTH, bg='orange').grid(row=0, column=1)
        Label(self.header, text='Name', width=self.NAME_WIDTH, bg='orange').grid(row=0, column=2)
        Label(self.header, text='Addon', width=self.ADDON_WIDTH, bg='orange').grid(row=0, column=3)
        Label(self.header, text='Total', width=self.TOTAL_WIDTH, bg='orange').grid(row=0, column=4)
        chkout_button1 = Button(self.chk_lower, width=BTN_WIDTH, height=BTN_HEIGHT, text="Edit Order", command=lambda: self.button_handler(3))
        chkout_button2 = Button(self.chk_lower, width=BTN_WIDTH, height=BTN_HEIGHT, text="Confirm Order", command=lambda: self.button_handler(7))

        # Checkout Frame 2
        self.custo_info = Frame(parent, padx=175, pady=75)
        chkout_dine_btn = Radiobutton(self.chk_lower2, text='Take Away', var=self.status_var, value='Take Away', command=lambda: self.button_handler(9), anchor='w', width=BTN_WIDTH)
        chkout_take_btn = Radiobutton(self.chk_lower2, text='Delivery ($5 Delivery Fee)', var=self.status_var, value='Delivery', command=lambda: self.button_handler(10), anchor='w', width=BTN_WIDTH)
        vcmd2 = (self.custo_info.register(self.callback))
        self.p_num_entry = Entry(self.chk_lower2, validate="key", validatecommand=(vcmd2, '%P'), state='disabled')
        back_btn = Button(self.chk_lower2, text='Back', command=lambda: self.button_handler(6), width=BTN_WIDTH, height=BTN_HEIGHT)
        confirm_btn = Button(self.chk_lower2, text='Finalize', command=lambda: self.button_handler(8), width=BTN_WIDTH, height=BTN_HEIGHT)

        # Final Frame
        self.order_type_label = Label(self.custo_info, text='Order Type: ', )
        self.p_num_label = Label(self.custo_info, text='Phone Number: ')
        self.final_grand_label = Label(self.custo_info, text='Grand Total: $0.00')
        chkout_back_btn = Button(self.custo_info, text='Back', command=lambda: self.button_handler(11), width=BTN_WIDTH, height=BTN_HEIGHT)
        chkout_confirm_btn = Button(self.custo_info, text='Place Order', command=lambda: self.button_handler(12), width=BTN_WIDTH, height=BTN_HEIGHT)
        self.final_frame = Frame(parent)
        self.final_label = Label(self.final_frame, text='Thank you again for choosing us! \n Your order will arrive soon. (when we feel like it)', font=("Arial", 15), width=45, height=15)

        self.title_frame.grid()
        title_label1.grid()
        self.name_entry.grid(pady=20)
        title_button.grid()

        self.main_label1.grid(row=0, column=0, sticky=EW)
        main_label2.grid(row=1, column=0, sticky=EW)
        self.order_wrapper.grid()
        self.button_frame.grid(sticky='we')
        self.button_frame.grid_columnconfigure(0, weight=1)
        self.button_frame.grid_columnconfigure(1, weight=1)
        self.button_frame.grid_propagate(0)
        self.create_widgets()
        self.destroy_widgets_button.grid(row=0, column=0)
        self.create_widgets_button.grid(row=0, column=1)
        main_button.grid(pady=30)

        self.header.grid()

        chkout_label1.grid()
        chkout_label2.grid()

        self.chk1.grid()
        self.chk2.grid()
        chkout_button1.grid(row=4, column=0, pady=30)
        chkout_button2.grid(row=4, column=1, pady=30)

        chkout_dine_btn.grid()
        chkout_take_btn.grid()
        self.p_num_entry.grid()
        back_btn.grid()
        confirm_btn.grid()
        self.p_num_label.grid()
        self.order_type_label.grid()
        self.final_grand_label.grid()
        chkout_back_btn.grid(pady=20)
        chkout_confirm_btn.grid()
        self.final_label.grid()

    def callback(self, p):
        """If input in entry field is a digit, allow to be entered else don't."""
        if str.isdigit(p) or p == "":
            return True
        else:
            return False
            
    def create_widgets(self):
        """Create the widgets for the order frame."""
        if self.count >= self.MAX_WIDGETS:
            self.create_widgets_button['state'] = 'disabled'
            self.destroy_widgets_button['state'] = 'normal'
            messagebox.showinfo(message="You have reached the maximum number of orders")
        else:
            """Dynamically create new keys for each widget created and assign to each widget as vars."""
            self.destroy_widgets_button['state'] = 'normal'
            self.count += 1
            self.dynamic_vars[f"self.order_var{self.count}"] = StringVar()
            self.dynamic_vars[f"self.addon_var{self.count}"] = StringVar()
            self.dynamic_vars[f"quantity_var{self.count}"] = IntVar()
            self.dynamic_vars[f"self.addon_var{self.count}"].set(str(self.addon_list[0]))
            self.dynamic_vars[f"self.order_var{self.count}"].set(str(self.MainItems_list[0]))

            frame = Frame(self.order_wrapper)
            self.frames.append(frame)

            vcmd = (frame.register(self.callback), '%P')
            qe = Entry(frame, textvariable=self.dynamic_vars[f"quantity_var{self.count}"], width=3, validate='key', validatecommand=(vcmd))
            order_drop = OptionMenu(frame, self.dynamic_vars[f"self.order_var{self.count}"], *self.MainItems_list)
            addon_drop = OptionMenu(frame, self.dynamic_vars[f"self.addon_var{self.count}"], *self.addon_list)

            self.widgets.append(qe)
            self.widgets.append(order_drop)
            self.widgets.append(addon_drop)

            frame.grid(sticky=EW, column=2, padx=80)
            qe.grid(row=0, column=0)
            order_drop.config(width=25)
            addon_drop.config(width=15)
            order_drop.grid(row=0, column=1, pady=2)
            addon_drop.grid(row=0, column=2)

    def remove_widgets(self):
        """Remove the widgets from the order frame."""
        if self.count <= self.MIN_WIDGETS:
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
        """
        Create a frame with label widgets for every item in self.current_orders. 
        Append the frame to a list and grid it.
        """
        self.ord_frames = []
        self.ord_wid = []

        self.grandtotal = 0
        for i in range(len(self.current_orders)):
            total = 0
            total += MainItems.total(self.current_orders[i])
            self.grandtotal += total
            order_frame = Frame(self.chk2, width=80, padx=50)
            self.ord_frames.append(order_frame)

            self.chkout_price_label = Label(order_frame, text=f'${self.current_orders[i].price}', width=self.PRICE_WIDTH, bg='peach puff')
            self.chkout_quantity_label = Label(order_frame, text=f'{self.current_orders[i].quantity}', width=self.QUANTITY_WIDTH, bg='peach puff')
            self.chkout_orders_label = Label(order_frame, text=self.current_orders[i].name, width=self.NAME_WIDTH, bg='peach puff')
            self.chkout_addons_label = Label(order_frame, text=self.current_orders[i].addons.name, width=self.ADDON_WIDTH, bg='peach puff')
            self.chkout_total_label = Label(order_frame, text=f'${total}', width=self.TOTAL_WIDTH, bg='peach puff')

            self.ord_wid.append(self.chkout_price_label)
            self.ord_wid.append(self.chkout_quantity_label)
            self.ord_wid.append(self.chkout_orders_label)
            self.ord_wid.append(self.chkout_addons_label)
            self.ord_wid.append(self.chkout_total_label)

            self.chkout_price_label.grid(row=1, column=0)
            self.chkout_quantity_label.grid(row=1, column=1)
            self.chkout_orders_label.grid(row=1, column=2)
            self.chkout_addons_label.grid(row=1, column=3)
            self.chkout_total_label.grid(row=1, column=4)
            self.ord_frames[i].grid()

        self.chkout_grand_label = Label(order_frame, text=f'GRAND TOTAL: ${self.grandtotal}', width=18, height=2)
        self.chkout_grand_label.grid(row=2, column=2)

    def button_handler(self, id):
        """Handle all button commands."""
        match id:
            case 1:
                """Add delay between switching from thanks to main frame."""
                self.thanks_label.configure(text=f'Thank you for choosing Burger Bar {self.name_entry.get()}!')
                self.main_label1.configure(text=f'Hello {self.name_entry.get()}!')
                self.title_frame.grid_forget()
                self.thanks_frame.grid()
                root.after(2000, self.thanks_frame.grid_forget)
                root.after(2100, self.main_frame.grid)
            case 2:
                """
                Loop through every order, take entry field input and add to designated var. 
                If quantity is 0, show warning and move to next item in loop.
                For every item in MainItems_list check if the item is equal to the order name, 
                  if it is, add the quantity to the item quantity and add the item to the current_orders list.
                If there are duplicate objects, create a deepcopy of the duplicate (treat it like a new object),
                  and add it to the list instead.
                For every item in addon_list check if the item is equal to the addon name, if it is, add the addon to the item.
                """
                try:
                    for i in range(self.count):
                        order_name = self.dynamic_vars[f"self.order_var{i+1}"].get()
                        addon_name = self.dynamic_vars[f"self.addon_var{i+1}"].get()
                        quantity = self.dynamic_vars[f"quantity_var{i+1}"].get()
                        if quantity == 0:
                            messagebox.showwarning(message="You can't have 0 of an item")
                            continue
                        else:
                            for item in self.MainItems_list:
                                if str(item) == order_name:
                                    item.quantity += quantity
                                    self.current_orders.append(item)
                                    print(self.current_orders)
                                    if self.current_orders.count(item) > 1:
                                        item.quantity -= quantity
                                        newitem = copy.deepcopy(item)
                                        newitem.quantity = quantity
                                        self.current_orders.remove(item)
                                        self.current_orders.append(newitem)
                                        for addon in self.addon_list:
                                            if str(addon) == addon_name:
                                                newitem.addons = addon
                                    else:
                                        for addon in self.addon_list:
                                            if str(addon) == addon_name:
                                                item.addons = addon
                    self.checkout_labels()
                    self.chk_lower.grid()
                    self.main_frame.grid_forget()
                    self.chkout_frame.grid(sticky=EW)
                except:
                    pass
            case 3:
                """Reset all variables and widgets to default."""
                self.current_orders = []
                for i in self.ord_frames:
                    i.destroy()
                for i in self.ord_wid:
                    i.destroy()
                for i in range(len(self.MainItems_list)):
                    if self.MainItems_list[i].quantity > 0:
                        self.MainItems_list[i].quantity = 0
                self.chkout_frame.grid_forget()
                self.main_frame.grid()
            case 4:
                """Create widgets for the checkout frame."""
                self.create_widgets()
            case 5:
                """Remove widgets from the checkout frame."""
                self.remove_widgets()
            case 6:
                """Reset Radiobuttons and Entry fields to default."""
                self.chk_lower2.grid_forget()
                self.chk_lower.grid()
                self.p_num_entry.delete(0, END)
                self.status_var.set('*')
            case 7:
                self.chk_lower2.grid()
                self.chk_lower.grid_forget()
            case 8:
                """
                Check if user has selected an order type and if they have entered a phone number. 
                If they have, create a Customer object and add it to the customer_list.
                """
                if self.status_var.get() == '*':
                    messagebox.showerror('Error', 'Please select an order type')
                elif self.status_var.get() == 'Delivery' and len(self.p_num_entry.get()) <= 2 or len(self.p_num_entry.get()) >= 14:
                    messagebox.showerror('Error', 'Please enter a phone number')
                else:
                    self.chkout_frame.grid_forget()
                    if self.status_var.get() == 'Delivery':
                        self.grandtotal += 5
                    person = Customer(self.name_entry.get(), self.status_var.get(), self.grandtotal, self.p_num_entry.get(), self.current_orders)
                    self.custo_info.grid()
                    if person.pnum:
                        self.p_num_label.configure(text=f'Phone Number: {person.pnum}')
                    else:
                        self.p_num_label.configure(text=f'Phone Number: N/A')
                    self.order_type_label.configure(text=f'Order Type: {person.status}')
                    self.final_grand_label.configure(text=f'Grand Total: ${person.sum}')
            case 9:
                self.p_num_entry.delete(0, END)
                self.p_num_entry.configure(state='disabled')
            case 10:
                self.p_num_entry.configure(state='normal')
            case 11:
                """Clear delivery fee."""
                self.custo_info.grid_forget()
                self.chkout_frame.grid()
                if self.status_var.get() == 'Delivery':
                    self.grandtotal -= 5
            case 12:
                self.custo_info.grid_forget()
                self.final_frame.grid()
                root.after(5000, exit)


"""Main Routine"""
if __name__ == "__main__":
    root = Tk()
    show_gui = OrderingGUI(root)
    root.geometry("500x350")
    root.mainloop()
