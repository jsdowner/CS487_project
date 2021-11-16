"""Module contains major customer classes"""
from tkinter import messagebox
import tkinter as tk
from tkinter.ttk import Treeview

#import db_manager as db
import login
import my_config

# Module Constants:
CUSTOMER_WINDOW_SIZE = "1028x500"

PRODUCT_COLUMNS = ('Id', 'Product name', 'Price', 'In stock')
PRODUCT_COLUMNS_SIZE = (25, 150, 50, 50)

MY_ORDERS_COLUMNS = ('Id', 'Product name', 'Quantity', 'Total price')
MY_ORDERS_COLUMNS_SIZE = (25, 150, 60, 90)


class CustomerApp:
    """Main customer window."""

    def __init__(self, master):
        """Initializes main customer window."""
        self.master = master
        self.master.geometry(CUSTOMER_WINDOW_SIZE)
        self.master.configure(bg=my_config.BACKGROUND)
        self.master.title(my_config.APP_NAME)

        # main frames
        self.frame = tk.Frame(self.master, bg=my_config.BACKGROUND, bd=15)
        self.function_frame = tk.Frame(self.master, bg=my_config.BACKGROUND)
        self.function_frame2 = tk.Frame(self.master, bg=my_config.BACKGROUND)


        # it contains error messages, for example not all entry are filled.
        self.error_label = tk.Label()

        self.product_tree = None
        self.my_orders_tree = None
        self.branch_entry = None
        self.quantity_entry = None
        self.id_product_entry = None
        
        self.entry_CustomerUsername = None
        self.entry_CustomerName = None
        self.entry_CustomerEmail = None
        self.entry_CustomerPhone = None
        self.entry_CustomerCC = None
        self.entry_CustomerExpDate = None
        self.entry_CustomerCCV = None

    def initialize_main_buttons(self):
        """Initializes main buttons"""
        if self.frame:
            self.frame.destroy()
        if self.function_frame:
            self.function_frame.destroy()

        self.frame = tk.Frame(self.master, bg=my_config.BACKGROUND)

        
        products_button = tk.Button(self.frame, text='View Products', bg=my_config.FOREGROUND,
#                                command=self.account_edit, width=16)
                                command=self.list_products, width=16)
        products_button.grid(row=1, column=0, pady=(0, 3))
        edit_button = tk.Button(self.frame, text='Edit Account', bg=my_config.FOREGROUND,
#                                command=self.account_edit, width=16)
                                command=self.update_customer, width=16)
        edit_button.grid(row=2, column=0, pady=(0, 3))
        orders_button = tk.Button(self.frame, text='My Orders', bg=my_config.FOREGROUND,
#                                  command=self.my_orders, width=16)
                                  command=self.new_page, width=16)
        orders_button.grid(row=3, column=0, pady=(0, 3))
        logoff_button = tk.Button(self.frame, text='Log Off', bg=my_config.FOREGROUND,
#                                  command=self.log_off, width=16)
                                  command=self.log_off, width=16)
        logoff_button.grid(row=4, column=0, pady=(0, 3))
        button_close = tk.Button(self.frame, text="Close Window", command=self.frame.destroy)#.pack()
        self.frame.pack()
        
        
        
    def update_customer(self):
        if self.frame:
            self.frame.destroy()
        if self.function_frame:
            self.function_frame.destroy()
        self.function_frame = tk.Frame(self.master, bg=my_config.BACKGROUND)
        
        """Allows user to update inventory"""

        # creating labels
        label_CustomerUsername = tk.Label(self.function_frame, text='Username:', bg=my_config.BACKGROUND, fg=my_config.FOREGROUND)
        label_CustomerUsername.grid(row=0, column=0, sticky=tk.E)
        label_CustomerName = tk.Label(self.function_frame, text='Name:', bg=my_config.BACKGROUND, fg=my_config.FOREGROUND)
        label_CustomerName.grid(row=1, column=0, sticky=tk.E)
        label_CustomerEmail = tk.Label(self.function_frame, text='Email:', bg=my_config.BACKGROUND, fg=my_config.FOREGROUND)
        label_CustomerEmail.grid(row=2, column=0, sticky=tk.E)
        label_CustomerPhone = tk.Label(self.function_frame, text='Phone:', bg=my_config.BACKGROUND, fg=my_config.FOREGROUND)
        label_CustomerPhone.grid(row=3, column=0, sticky=tk.E)
        label_CustomerCC = tk.Label(self.function_frame, text='Credit Card Number:', bg=my_config.BACKGROUND, fg=my_config.FOREGROUND)
        label_CustomerCC.grid(row=4, column=0, sticky=tk.E)
        label_CustomerExpDate = tk.Label(self.function_frame, text='Expiration Date:', bg=my_config.BACKGROUND, fg=my_config.FOREGROUND)
        label_CustomerExpDate.grid(row=5, column=0, sticky=tk.E)
        label_CustomerCCV = tk.Label(self.function_frame, text='CCV:', bg=my_config.BACKGROUND, fg=my_config.FOREGROUND)
        label_CustomerCCV.grid(row=6, column=0, sticky=tk.E)

        # creating entry boxes
        self.entry_CustomerUsername = tk.Entry(self.function_frame, width=30, bg=my_config.FOREGROUND)
        self.entry_CustomerUsername.grid(row=0, column=1)
        self.entry_CustomerName = tk.Entry(self.function_frame, width=30, bg=my_config.FOREGROUND)
        self.entry_CustomerName.grid(row=1, column=1)
        self.entry_CustomerEmail = tk.Entry(self.function_frame, width=30, bg=my_config.FOREGROUND)
        self.entry_CustomerEmail.grid(row=2, column=1)
        self.entry_CustomerPhone = tk.Entry(self.function_frame, width=30, bg=my_config.FOREGROUND)
        self.entry_CustomerPhone.grid(row=3, column=1)
        self.entry_CustomerCC = tk.Entry(self.function_frame, width=30, bg=my_config.FOREGROUND)
        self.entry_CustomerCC.grid(row=4, column=1)
        self.entry_CustomerExpDate = tk.Entry(self.function_frame, width=30, bg=my_config.FOREGROUND)
        self.entry_CustomerExpDate.grid(row=5, column=1)
        self.entry_CustomerCCV = tk.Entry(self.function_frame, width=30, bg=my_config.FOREGROUND)
        self.entry_CustomerCCV.grid(row=6, column=1)

        # buttons
        save_button = tk.Button(self.function_frame, text='Save Changes',
                                bg=my_config.FOREGROUND, command=self.new_page, width=16)
        save_button.grid(row=7, column=0)
                                 
        close_button = tk.Button(self.function_frame, text='Close',
                                 bg=my_config.FOREGROUND, command=self.initialize_main_buttons, width=16)
        close_button.grid(row=8, column=0)
 
        self.function_frame.pack()

        
    def list_products(self):
        """Lists all of the products"""

        # frame for listbox
        if self.frame:
            self.frame.destroy()
        if self.function_frame:
            self.function_frame.destroy()
        if self.function_frame2:
            self.function_frame2.destroy()
            
            
        self.function_frame = tk.Frame(self.master, bg=my_config.BACKGROUND)
        self.function_frame2 = tk.Frame(self.master, bg=my_config.BACKGROUND)

        list_label = tk.Label(self.function_frame, text='List of Products',
                              width=100, bg=my_config.BACKGROUND)
        list_label.grid(row=0, column=0, pady=(10, 0))

        # creating treeview for customers
        self.product_tree = Treeview(self.function_frame, columns=PRODUCT_COLUMNS,
                                     show='headings', height=10)
        self.product_tree.grid(row=1, column=0, padx=8)

        for column_name, width in zip(PRODUCT_COLUMNS, PRODUCT_COLUMNS_SIZE):
            self.product_tree.column(column_name, width=width, anchor=tk.CENTER)
            self.product_tree.heading(column_name, text=column_name)

        #scrollbar = tk.Scrollbar(self.function_frame, orient=tk.VERTICAL)
        #scrollbar.configure(command=self.product_tree.set)
        #self.product_tree.configure(yscrollcommand=scrollbar)
        #self.product_tree.bind('<ButtonRelease-1>', self.product_selection)

#         # adding records from DB to Listbox
#         records = db.return_products()
#         for record in records:
#             self.product_tree.insert('', tk.END, values=[record[0], record[1], record[2], record[3]])


        # buttons
        place_order_button = tk.Button(self.function_frame, text='Place order',
                                       bg=my_config.FOREGROUND, command=self.place_order, width=16)
        place_order_button.grid(row=4, column=0)
        close_button = tk.Button(self.function_frame, text='Return to Customer Menu',
                                   bg=my_config.FOREGROUND, command=self.initialize_main_buttons, width=16)
        close_button.grid(row=5, column=0)

        
        self.function_frame.pack()
        
    def place_order(self):
        """Lists all of the products"""

        # frame for listbox
        if self.frame:
            self.frame.destroy()
        if self.function_frame:
            self.function_frame.destroy()      
        self.function_frame = tk.Frame(self.master, bg=my_config.BACKGROUND)

            

        # creating labels
        id_product_label = tk.Label(self.function_frame, text='Product ID:', fg=my_config.FOREGROUND, bg=my_config.BACKGROUND)
        id_product_label.grid(row=0, column=0, sticky=tk.E)
        quantity_label = tk.Label(self.function_frame, text='Quantity:', fg=my_config.FOREGROUND, bg=my_config.BACKGROUND)
        quantity_label.grid(row=1, column=0, sticky=tk.E)
        location_label = tk.Label(self.function_frame, text='Branch:', fg=my_config.FOREGROUND, bg=my_config.BACKGROUND)
        location_label.grid(row=2, column=0, sticky=tk.E)

        # creating entry boxes
        self.id_product_entry = tk.Entry(self.function_frame, width=30, bg=my_config.FOREGROUND)
        self.id_product_entry.grid(row=0, column=1)
        self.quantity_entry = tk.Entry(self.function_frame, width=30, bg=my_config.FOREGROUND)
        self.quantity_entry.grid(row=1, column=1)
        self.branch_entry = tk.Entry(self.function_frame, width=30, bg=my_config.FOREGROUND)
        self.branch_entry.grid(row=2, column=1)

        # buttons
        place_order_button = tk.Button(self.function_frame, text='Add to Cart',
                                       bg=my_config.FOREGROUND, command=self.new_page, width=16)
        place_order_button.grid(row=4, column=0)
        close_button = tk.Button(self.function_frame, text='Return to Customer Menu',
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
        """Returns customer to login window."""
        if self.frame:
            self.frame.destroy()
        if self.function_frame:
            self.function_frame.destroy()
        if self.function_frame2:
            self.function_frame2.destroy()
        application = login.LoginWindow(self.master)
        application.initialize_login_window()