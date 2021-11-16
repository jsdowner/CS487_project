"""Module contains major customer classes"""
from tkinter import messagebox
import tkinter as tk
from tkinter.ttk import Treeview

#import db_manager as db
import login
import my_config

# Module Constants:
EMPLOYEE_WINDOW_SIZE = "1028x500"

PRODUCT_COLUMNS = ('Id', 'Product name', 'Branch', 'Quantity')
PRODUCT_COLUMNS_SIZE = (25, 150, 50, 60)

CUSTOMER_COLUMNS = ('Username', 'Name', 'Email', 'Phone')
CUSTOMER_COLUMNS_SIZE = (25, 150, 60, 60)


class EmployeeApp:
    """Main employee window."""

    def __init__(self, master):
        """Initializes main customer window."""
        self.master = master
        self.master.geometry(EMPLOYEE_WINDOW_SIZE)
        self.master.configure(bg=my_config.BACKGROUND)
        self.master.title(my_config.APP_NAME)

        # main frames
        self.frame = tk.Frame(self.master, bg=my_config.BACKGROUND, bd=15)
        self.function_frame = tk.Frame(self.master, bg=my_config.BACKGROUND)
        self.function_frame2 = tk.Frame(self.master, bg=my_config.BACKGROUND)


        # it contains error messages, for example not all entry are filled.
        self.error_label = tk.Label()

        self.product_tree = None
        self.entry_ProductID = None
        self.entry_ProductName = None
        self.entry_ProductBranch = None
        self.entry_ProductQuantity = None
        
        self.customer_tree = None
        self.entry_CustomerUsername = None
        self.entry_CustomerName = None
        self.entry_CustomerEmail = None
        self.entry_CustomerPhone = None
        
        self.entry_EmployeeUsername = None
        self.entry_EmployeeName = None
        self.entry_EmployeeEmail = None
        self.entry_EmployeePhone = None
        self.entry_EmployeeBranch = None


    def initialize_main_buttons(self):
        """Initializes main buttons"""
        if self.frame:
            self.frame.destroy()
        if self.function_frame:
            self.function_frame.destroy()

        self.frame = tk.Frame(self.master, bg=my_config.BACKGROUND)
        self.frame.title = "Employee Menu"

        edit_button = tk.Button(self.frame, text='Edit account', bg=my_config.FOREGROUND,
#                                command=self.account_edit, width=16)
                                command=self.update_employee, width=16)
        edit_button.grid(row=1, column=0, pady=(0, 3))
        inventory_button = tk.Button(self.frame, text='Inventory', bg=my_config.FOREGROUND,
#                                  command=self.inventory, width=16)
                                  command=self.show_inventory, width=16)
        inventory_button.grid(row=2, column=0, pady=(0, 3))
        
        customers_button = tk.Button(self.frame, text='Customers', bg=my_config.FOREGROUND, command=self.show_customers, width=16)
        customers_button.grid(row=3, column=0, pady=(0, 3))
        
        logoff_button = tk.Button(self.frame, text='Log Off', bg=my_config.FOREGROUND, command=self.log_off, width=16)
        logoff_button.grid(row=4, column=0, pady=(0, 3))
        
        self.frame.pack()

        
    def update_employee(self):
        if self.frame:
            self.frame.destroy() 
        if self.function_frame:
            self.function_frame.destroy() 
        self.function_frame = tk.Frame(self.master, bg=my_config.BACKGROUND)
        
        """Allows employee to update his/her own information"""

        # creating labels
        label_EmployeeUsername = tk.Label(self.function_frame, text='Username:', bg=my_config.BACKGROUND, fg=my_config.FOREGROUND)
        label_EmployeeUsername.grid(row=0, column=0, sticky=tk.E)
        label_EmployeeName = tk.Label(self.function_frame, text='Name:', bg=my_config.BACKGROUND, fg=my_config.FOREGROUND)
        label_EmployeeName.grid(row=1, column=0, sticky=tk.E)
        label_EmployeeEmail = tk.Label(self.function_frame, text='Email:', bg=my_config.BACKGROUND, fg=my_config.FOREGROUND)
        label_EmployeeEmail.grid(row=2, column=0, sticky=tk.E)
        label_EmployeePhone = tk.Label(self.function_frame, text='Phone:', bg=my_config.BACKGROUND, fg=my_config.FOREGROUND)
        label_EmployeePhone.grid(row=3, column=0, sticky=tk.E)
        label_EmployeeBranch = tk.Label(self.function_frame, text='Branch:', bg=my_config.BACKGROUND, fg=my_config.FOREGROUND)
        label_EmployeeBranch.grid(row=4, column=0, sticky=tk.E)

        # creating entry boxes
        self.entry_EmployeeUsername = tk.Entry(self.function_frame, width=30, bg=my_config.FOREGROUND)
        self.entry_EmployeeUsername.grid(row=0, column=1)
        self.entry_EmployeeName = tk.Entry(self.function_frame, width=30, bg=my_config.FOREGROUND)
        self.entry_EmployeeName.grid(row=1, column=1)
        self.entry_EmployeeEmail = tk.Entry(self.function_frame, width=30, bg=my_config.FOREGROUND)
        self.entry_EmployeeEmail.grid(row=2, column=1)
        self.entry_EmployeePhone = tk.Entry(self.function_frame, width=30, bg=my_config.FOREGROUND)
        self.entry_EmployeePhone.grid(row=3, column=1)
        self.entry_EmployeeBranch = tk.Entry(self.function_frame, width=30, bg=my_config.FOREGROUND)
        self.entry_EmployeeBranch.grid(row=4, column=1)

        # buttons
        save_button = tk.Button(self.function_frame, text='Save Changes',
                                bg=my_config.FOREGROUND, command=self.new_page, width=16)
        save_button.grid(row=5, column=0)
                                 
        close_button = tk.Button(self.function_frame, text='Close',
                                 bg=my_config.FOREGROUND, command=self.initialize_main_buttons, width=16)
        close_button.grid(row=6, column=0)
 
        self.function_frame.pack()
        
    def show_inventory(self):
        if self.frame:
            self.frame.destroy()
        if self.function_frame:
            self.function_frame.destroy()

        """Lists all of the inventory"""

        # frame for listbox
        self.function_frame = tk.Frame(self.master, bg=my_config.BACKGROUND)

        list_label = tk.Label(self.function_frame, text='Inventory', width=100, bg=my_config.BACKGROUND)
        list_label.grid(row=0, column=0, pady=(10, 0))

        # creating treeview for customers
        self.product_tree = Treeview(self.function_frame, columns=PRODUCT_COLUMNS, show='headings', height=10)
        self.product_tree.grid(row=1, column=0, padx=8)

        for column_name, width in zip(PRODUCT_COLUMNS, PRODUCT_COLUMNS_SIZE):
            self.product_tree.column(column_name, width=width, anchor=tk.CENTER)
            self.product_tree.heading(column_name, text=column_name)



        update_inventory_button = tk.Button(self.function_frame, text='Update Inventory',
                                            bg=my_config.FOREGROUND, command=self.update_inventory, width=16)
        update_inventory_button.grid(row=4, column=0)
        close_button = tk.Button(self.function_frame, text='Employee Menu',
                                 bg=my_config.FOREGROUND, command=self.initialize_main_buttons, width=16)
        close_button.grid(row=5, column=0)
 
 
        self.function_frame.pack()
        
        
    def update_inventory(self):
        if self.frame:
            self.frame.destroy()
        if self.function_frame:
            self.function_frame.destroy()
            
        self.function_frame = tk.Frame(self.master, bg=my_config.BACKGROUND)
        """Allows employee to update inventory"""
#        self.initialize_main_buttons()

        # creating labels
        label_ProductID = tk.Label(self.function_frame, text='Product ID:', bg=my_config.BACKGROUND, fg=my_config.FOREGROUND)
        label_ProductID.grid(row=0, column=0, sticky=tk.E)
        label_ProductName = tk.Label(self.function_frame, text='Product Name:', bg=my_config.BACKGROUND, fg=my_config.FOREGROUND)
        label_ProductName.grid(row=1, column=0, sticky=tk.E)
        label_ProductBranch = tk.Label(self.function_frame, text='Branch:', bg=my_config.BACKGROUND, fg=my_config.FOREGROUND)
        label_ProductBranch.grid(row=2, column=0, sticky=tk.E)
        label_ProductQuantity = tk.Label(self.function_frame, text='Quantity:', bg=my_config.BACKGROUND, fg=my_config.FOREGROUND)
        label_ProductQuantity.grid(row=3, column=0, sticky=tk.E)

        # creating entry boxes
        self.entry_ProductID = tk.Entry(self.function_frame, width=30, bg=my_config.FOREGROUND)
        self.entry_ProductID.grid(row=0, column=1)
        self.entry_ProductName = tk.Entry(self.function_frame, width=30, bg=my_config.FOREGROUND)
        self.entry_ProductName.grid(row=1, column=1)
        self.entry_ProductBranch = tk.Entry(self.function_frame, width=30, bg=my_config.FOREGROUND)
        self.entry_ProductBranch.grid(row=2, column=1)
        self.entry_ProductQuantity = tk.Entry(self.function_frame, width=30, bg=my_config.FOREGROUND)
        self.entry_ProductQuantity.grid(row=3, column=1)

        # buttons
        save_button = tk.Button(self.function_frame, text='Save Changes',
                                bg=my_config.FOREGROUND, command=self.new_page, width=16)
        save_button.grid(row=4, column=0)
        close_button = tk.Button(self.function_frame, text='Close',
                                 bg=my_config.FOREGROUND, command=self.initialize_main_buttons, width=16)
        close_button.grid(row=5, column=0)
 
        self.function_frame.pack()
        
        
    def show_customers(self):
        """Lists all of the customers"""
        # frame for listbox
        if self.frame:
            self.frame.destroy()
        if self.function_frame:
            self.function_frame.destroy()
        self.function_frame = tk.Frame(self.master, bg=my_config.BACKGROUND)

        list_label = tk.Label(self.function_frame, text='Customers', width=100, bg=my_config.BACKGROUND)
        list_label.grid(row=0, column=0, pady=(10, 0))

        # creating treeview for customers
        self.customer_tree = Treeview(self.function_frame, columns=CUSTOMER_COLUMNS, show='headings', height=10)
        self.customer_tree.grid(row=1, column=0, padx=8)

        for column_name, width in zip(CUSTOMER_COLUMNS, CUSTOMER_COLUMNS_SIZE):
            self.customer_tree.column(column_name, width=width, anchor=tk.CENTER)
            self.customer_tree.heading(column_name, text=column_name)

        # buttons
        update_customers_button = tk.Button(self.function_frame, text='Update Customer(s)',
                                       bg=my_config.FOREGROUND, command=self.update_customer, width=16)
        update_customers_button.grid(row=4, column=0)
        close_button = tk.Button(self.function_frame, text='Employee Menu',
                                       bg=my_config.FOREGROUND, command=self.initialize_main_buttons, width=16)
        close_button.grid(row=5, column=0)
 
        self.function_frame.pack()
    
    def update_customer(self):
        if self.frame:
            self.frame.destroy()
        if self.function_frame:
            self.function_frame.destroy()
            
        self.function_frame = tk.Frame(self.master, bg=my_config.BACKGROUND)
        
        """Allows employee to update customers"""

        # creating labels
        label_CustomerUsername = tk.Label(self.function_frame, text='Username:', bg=my_config.BACKGROUND, fg=my_config.FOREGROUND)
        label_CustomerUsername.grid(row=0, column=0, sticky=tk.E)
        label_CustomerName = tk.Label(self.function_frame, text='Name:', bg=my_config.BACKGROUND, fg=my_config.FOREGROUND)
        label_CustomerName.grid(row=1, column=0, sticky=tk.E)
        label_CustomerEmail = tk.Label(self.function_frame, text='Email:', bg=my_config.BACKGROUND, fg=my_config.FOREGROUND)
        label_CustomerEmail.grid(row=2, column=0, sticky=tk.E)
        label_CustomerPhone = tk.Label(self.function_frame, text='Phone:', bg=my_config.BACKGROUND, fg=my_config.FOREGROUND)
        label_CustomerPhone.grid(row=3, column=0, sticky=tk.E)

        # creating entry boxes
        self.entry_CustomerUsername = tk.Entry(self.function_frame, width=30, bg=my_config.FOREGROUND)
        self.entry_CustomerUsername.grid(row=0, column=1)
        self.entry_CustomerName = tk.Entry(self.function_frame, width=30, bg=my_config.FOREGROUND)
        self.entry_CustomerName.grid(row=1, column=1)
        self.entry_CustomerEmail = tk.Entry(self.function_frame, width=30, bg=my_config.FOREGROUND)
        self.entry_CustomerEmail.grid(row=2, column=1)
        self.entry_CustomerPhone = tk.Entry(self.function_frame, width=30, bg=my_config.FOREGROUND)
        self.entry_CustomerPhone.grid(row=3, column=1)

        # buttons
        save_button = tk.Button(self.function_frame, text='Save Changes',
                                bg=my_config.FOREGROUND, command=self.new_page, width=16)
        save_button.grid(row=4, column=0)
                                 
        close_button = tk.Button(self.function_frame, text='Close',
                                 bg=my_config.FOREGROUND, command=self.initialize_main_buttons, width=16)
        close_button.grid(row=5, column=0)
 
        self.function_frame.pack()
        
        
    def new_page(self):
        top_new = tk.Toplevel()
        top_new.geometry("1028x500")
        top_new.title("new page")

        #_________ "Hello World" Label _________ 

        label_helloWorld = tk.Label(top_new, text="Hello World").pack()

        #_________ Close Button _________ 

        button_close = tk.Button(top_new, text="Close Window", command=top_new.destroy).pack()
        
    def log_off(self):
        """Returns Employee to login window."""
        if self.frame:
            self.frame.destroy()
        if self.function_frame:
            self.function_frame.destroy()
        application = login.LoginWindow(self.master)
        application.initialize_login_window()