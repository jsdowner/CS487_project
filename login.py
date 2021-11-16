"""Login and create new acc module."""
import tkinter as tk
import my_config
import Customer_View
import Employee_View
import Manager_View


# Module Constants:
LOGIN_WINDOW_SIZE = "1028x500"
FALSE_LOG_IN_VALUE = -1

class LoginWindow:
    """Login and create new acc window."""

    def __init__(self, master):
        """Creates login window."""
        self.master = master
        self.master.title(my_config.APP_NAME)
        self.master.geometry(LOGIN_WINDOW_SIZE)
        self.master.configure(bg=my_config.BACKGROUND)
        self.function_frame = tk.Frame(self.master, bg=my_config.BACKGROUND, bd=15)
        self.frame = tk.Frame(self.master, bg=my_config.BACKGROUND, bd=15)

        # it contains error messages, for example not all entry are filled.
        self.error_label = tk.Label()

        # class entries
        self.entry_Username = None
        self.entry_Password = None
        self.entry_UserType = None
       
        self.customer_tree = None
        self.entry_CustomerUsername = None
        self.entry_CustomerName = None
        self.entry_CustomerEmail = None
        self.entry_CustomerPhone = None
        
        self.employee_tree = None
        self.entry_EmployeeUsername = None
        self.entry_EmployeeName = None
        self.entry_EmployeeEmail = None
        self.entry_EmployeePhone = None
        self.entry_EmployeeBranch = None
        
        self.entry_ManagerUsername = None
        self.entry_ManagerName = None
        self.entry_ManagerEmail = None
        self.entry_ManagerPhone = None
        self.entry_ManagerBranch = None
        
        
    def initialize_login_window(self):
        """Initializing login window."""
        if self.function_frame:
            self.function_frame.destroy()
        if self.frame:
            self.frame.destroy()
        self.frame = tk.Frame(self.master, bg=my_config.BACKGROUND, bd=15)

        # username, password, user type
        label_Username = tk.Label(self.frame, bg=my_config.BACKGROUND, text='Username:', fg= my_config.FOREGROUND)
        label_Username.grid(row=0, column=0)
        self.entry_Username = tk.Entry(self.frame, bg=my_config.FOREGROUND, width=18)
        self.entry_Username.grid(row=0, column=1)
        
        label_Password = tk.Label(self.frame, bg=my_config.BACKGROUND, text='Password:', fg = my_config.FOREGROUND)
        label_Password.grid(row=1, column=0)
        self.entry_Password = tk.Entry(self.frame, show='*', bg=my_config.FOREGROUND, width=18)
        self.entry_Password.grid(row=1, column=1)
        
        label_UserType = tk.Label(self.frame, bg=my_config.BACKGROUND,
                                  text= 'User Type (\"Customer\", \"Employee\", \"Manager)\": ', fg = my_config.FOREGROUND)
        label_UserType.grid(row=2, column=0)
        self.entry_UserType = tk.Entry(self.frame, bg=my_config.FOREGROUND, width=18)
        self.entry_UserType.grid(row=2, column=1)

        # login, create account buttons
        login_button = tk.Button(self.frame, text='Log in', bg=my_config.FOREGROUND,command=self.login, width=16)
        login_button.grid(row=5, column=1, pady=(10, 0))
        create_button = tk.Button(self.frame, text='Create Account',bg=my_config.FOREGROUND, command=self.create_account_prompt, width=16)
        create_button.grid(row=10, column=1, pady=(10,0))
        self.frame.pack()
        
    def login(self):
        """Method that runs admin/customer, depending on permissions"""
        # deleting error label from last add_order call, if it exists
        if self.frame:
            self.frame.destroy()
        if self.function_frame:
            self.function_frame.destroy()
        self.frame = tk.Frame(self.master, bg=my_config.BACKGROUND, bd=15)

        if self.error_label:
            self.error_label.destroy()

        # checking if all required entries are filled
        if not self.entry_Username.get():
            self.error_label = tk.Label(self.frame, text="Username missing",
                                        fg=my_config.ERROR_FOREGROUND, bg=my_config.BACKGROUND)
            self.error_label.grid(row=2, column=1)
        elif not self.entry_Password.get():
            self.error_label = tk.Label(self.frame, text="Password missing",
                                        fg=my_config.ERROR_FOREGROUND, bg=my_config.BACKGROUND)
            self.error_label.grid(row=2, column=1)
        elif self.entry_UserType.get() == 'Customer':
            self.customer_app()
        elif self.entry_UserType.get() == 'Employee':
            self.employee_app()
        elif self.entry_UserType.get() == 'Manager':
            self.manager_app()
        else:
            self.error_label = tk.Label(self.frame, text="Invalid User Type (note: case sensitive)",
                                        fg=my_config.ERROR_FOREGROUND, bg=my_config.BACKGROUND)
            self.error_label.grid(row=2, column=1)


#         else:
# #             my_config.MY_ID, perm = db.customer_perm(self.username_entry.get(), self.password_entry.get())
# #             if perm == FALSE_LOG_IN_VALUE or my_config.MY_ID == FALSE_LOG_IN_VALUE:
# #                 self.error_label = tk.Label(self.frame, text="try again..",
# #                                             fg=my_config.ERROR_FOREGROUND, bg=my_config.BACKGROUND)
# #                 self.error_label.grid(row=2, column=1)
# #             elif perm == my_config.ADMIN_PERM:
# #                 self.admin_app()
# #             else:
# #                 self.customer_app()
#             self.customer_app()
        #self.new_page()
        self.frame.pack()
        

        
    def create_account_prompt(self):
        if self.frame:
            self.frame.destroy()
        if self.function_frame:
            self.function_frame.destroy()
        self.function_frame = tk.Frame(self.master, bg=my_config.BACKGROUND)
        
        label_UserType = tk.Label(self.function_frame,
                                  text='User Type (\'Customer\', \'Employee\', or \'Manager\'):',
                                  bg=my_config.BACKGROUND, fg=my_config.FOREGROUND)
        label_UserType.grid(row=0, column=0, sticky=tk.E)
        
        self.entry_UserType = tk.Entry(self.function_frame, width=30, bg=my_config.FOREGROUND)
        self.entry_UserType.grid(row=0, column=1)
        
        create_button = tk.Button(self.function_frame, text='Create Account', bg=my_config.FOREGROUND,
                                 command=self.create_account, width=16)
        create_button.grid(row=5, column=1, pady=(10, 0))
        self.function_frame.pack()
        
        
    def create_account(self):
        """Method that runs admin/customer, depending on permissions"""
        # deleting error label from last add_order call, if it exists
        if self.frame:
            self.frame.destroy()
        self.frame = tk.Frame(self.master, bg=my_config.BACKGROUND)
        if self.error_label:
            self.error_label.destroy()

        # checking if all required entries are filled
        if not self.entry_UserType.get():
            self.error_label = tk.Label(self.frame, text="User Type Missing",
                                        fg=my_config.ERROR_FOREGROUND, bg=my_config.BACKGROUND)
            self.error_label.grid(row=2, column=1)

        elif self.entry_UserType.get() == 'Customer':
            self.create_account_customer()
        elif self.entry_UserType.get() == 'Employee':
            self.create_account_employee()
        elif self.entry_UserType.get() == 'Manager':
            self.create_account_manager()
        else:
            self.error_label = tk.Label(self.frame, text="Invalid User Type (note: case sensitive)",
                                        fg=my_config.ERROR_FOREGROUND, bg=my_config.BACKGROUND)
            self.error_label.grid(row=2, column=1)
            self.create_account_prompt()
            
        #self.frame.pack()
        
        
    def create_account_customer(self):
        if self.frame:
            self.frame.destroy()
        if self.function_frame:
            self.function_frame.destroy()
        self.function_frame = tk.Frame(self.master, bg=my_config.BACKGROUND)
        
        """Allows user to create account"""

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
                                 
        close_button = tk.Button(self.function_frame, text='Back to Login Page',
                                 bg=my_config.FOREGROUND, command=self.initialize_login_window, width=16)
        close_button.grid(row=8, column=0)
 
        self.function_frame.pack()
    
    def create_account_employee(self):
        if self.frame:
            self.frame.destroy()
        if self.function_frame:
            self.function_frame.destroy() 
        self.function_frame = tk.Frame(self.master, bg=my_config.BACKGROUND)
        
        """Allows employee to create account"""

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
        save_button.grid(row=4, column=0)
                                 
        close_button = tk.Button(self.function_frame, text='Back to Login Page',
                                 bg=my_config.FOREGROUND, command=self.initialize_login_window, width=16)
        close_button.grid(row=5, column=0)
 
        self.function_frame.pack()
    
    def create_account_manager(self):
        if self.frame:
            self.frame.destroy()
        if self.function_frame:
            self.function_frame.destroy()  
        self.function_frame = tk.Frame(self.master, bg=my_config.BACKGROUND)
        
        """Allows manager to create account"""

        # creating labels
        label_ManagerUsername = tk.Label(self.function_frame, text='Username:', bg=my_config.BACKGROUND, fg=my_config.FOREGROUND)
        label_ManagerUsername.grid(row=0, column=0, sticky=tk.E)
        label_ManagerName = tk.Label(self.function_frame, text='Name:', bg=my_config.BACKGROUND, fg=my_config.FOREGROUND)
        label_ManagerName.grid(row=1, column=0, sticky=tk.E)
        label_ManagerEmail = tk.Label(self.function_frame, text='Email:', bg=my_config.BACKGROUND, fg=my_config.FOREGROUND)
        label_ManagerEmail.grid(row=2, column=0, sticky=tk.E)
        label_ManagerPhone = tk.Label(self.function_frame, text='Phone:', bg=my_config.BACKGROUND, fg=my_config.FOREGROUND)
        label_ManagerPhone.grid(row=3, column=0, sticky=tk.E)
        label_ManagerBranch = tk.Label(self.function_frame, text='Branch:', bg=my_config.BACKGROUND, fg=my_config.FOREGROUND)
        label_ManagerBranch.grid(row=4, column=0, sticky=tk.E)

        # creating entry boxes
        self.entry_ManagerUsername = tk.Entry(self.function_frame, width=30, bg=my_config.FOREGROUND)
        self.entry_ManagerUsername.grid(row=0, column=1)
        self.entry_ManagerName = tk.Entry(self.function_frame, width=30, bg=my_config.FOREGROUND)
        self.entry_ManagerName.grid(row=1, column=1)
        self.entry_ManagerEmail = tk.Entry(self.function_frame, width=30, bg=my_config.FOREGROUND)
        self.entry_ManagerEmail.grid(row=2, column=1)
        self.entry_ManagerPhone = tk.Entry(self.function_frame, width=30, bg=my_config.FOREGROUND)
        self.entry_ManagerPhone.grid(row=3, column=1)
        self.entry_ManagerBranch = tk.Entry(self.function_frame, width=30, bg=my_config.FOREGROUND)
        self.entry_ManagerBranch.grid(row=4, column=1)

        # buttons
        save_button = tk.Button(self.function_frame, text='Save Changes',
                                bg=my_config.FOREGROUND, command=self.new_page, width=16)
        save_button.grid(row=4, column=0)
                                 
        close_button = tk.Button(self.function_frame, text='Back to Login Page',
                                 bg=my_config.FOREGROUND, command=self.initialize_login_window, width=16)
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
        
    def customer_app(self):
        self.frame.destroy()
        application = Customer_View.CustomerApp(self.master)
        application.initialize_main_buttons()

        
    def employee_app(self):
        self.frame.destroy()
        application = Employee_View.EmployeeApp(self.master)
        application.initialize_main_buttons()
        
        
    def manager_app(self):
        self.frame.destroy()
        application = Manager_View.ManagerApp(self.master)
        application.initialize_main_buttons()
        