from tkinter import *
from tkinter import messagebox

class ordering_items:
    """Order Items Object"""
    def __init__(self, name, price, type):
        self.name = name
        self.price = price
        self.type = type
class customer:
    """Customer Object"""
    def __init__(self, name, status):
        self.name = name
        self.status = status
    
class ordering_gui:
    """Main GUI class"""
    def __init__(self, parent):
        #Initialise the title frame
        
        ordering_items_list = [ordering_items('A', 1.00, 'main'), ordering_items('B', 2.00, 'main'), ordering_items('C', 3.00, 'main')]
        addon_list = [ordering_items('Addon A', 0.5, 'addon'), ordering_items('Addon B', 0.75, 'addon'), ordering_items('Addon C', 1.00, 'addon')]
        self.customer_list = []
        
        self.order_var = StringVar()
        self.addon_var = StringVar()
        self.order_var.set(ordering_items_list[0].name)
        self.addon_var.set(addon_list[0].name)
        self.title_frame = Frame(parent)
        title_label_1 = Label(self.title_frame, text="Welcome to (Company Name inc.)")
        self.name_entry = Entry(self.title_frame)
        
        title_button = Button(self.title_frame, text="Confirm", command=self.title_button_command)
        
        self.title_frame.grid()
        title_label_1.grid()
        self.name_entry.grid()
        title_button.grid()
        
        self.thanks_frame = Frame(parent)
        
        self.thanks_label = Label(self.thanks_frame, text=f'Thank you for choosing (Company Name inc.) !')
        
        self.thanks_label.grid()
        
        self.main_frame = Frame(parent)
        self.main_label_1 = Label(self.main_frame, text="Hello customer_name")
        main_label_2 = Label(self.main_frame, text="Your orders:")
        quantity_entry = Entry(self.main_frame, width=2)
        
        order_item_names = []
        addon_item_names = []
        for i in range(len(ordering_items_list)):
            order_item_names.append(ordering_items_list[i].name)
        for i in range(len(addon_list)):
            addon_item_names.append(addon_list[i].name)
        order_drop = OptionMenu(self.main_frame, self.order_var, *order_item_names)    
        addon_drop = OptionMenu(self.main_frame, self.addon_var, *addon_item_names)
       
        
        self.main_label_1.grid()
        main_label_2.grid()
        quantity_entry.grid()
        order_drop.grid()
        addon_drop.grid()
        
    def title_button_command(self):
        """Add delay between switching frames"""
        self.thanks_label.configure(text=f'Thank you for choosing (Company Name inc.) {self.name_entry.get()}!')
        self.main_label_1.configure(text=f'Hello {self.name_entry.get()}!')
        self.title_frame.grid_forget()
        self.thanks_frame.grid()
        root.after(2000, self.thanks_frame.grid_forget)
        root.after(2100, self.main_frame.grid)
      
     

"""Main Routine"""
if __name__ == "__main__":
    root = Tk()
    show_gui = ordering_gui(root)
    root.geometry("250x350")
    root.mainloop()