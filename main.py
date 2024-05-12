from customtkinter import *
from PIL import Image
import tkinter
import requests
from CTkTable import CTkTable
from CTkMessagebox import CTkMessagebox

class App(CTk):

    def __init__(self, **kw):
        super().__init__( **kw)
        self.geometry("750x550")
        self.resizable(0,0)
        set_appearance_mode("dark")

        self.build_sidebar_ui()

        self.main_view = CTkFrame(master=self, fg_color="#204B6B", corner_radius=0, width=580, height=550)
        self.main_view.pack_propagate(0)
        self.main_view.pack(side="left")

        self.switch_main_view("LOGIN")
        
    def build_sidebar_ui(self):
        sidebar_frame = CTkFrame(master=self, fg_color="#4385B7",  width=170, height=550, corner_radius=0)
        sidebar_frame.pack_propagate(0)
        sidebar_frame.pack(fill="y", anchor="w", side="left")

        logo_img_data = Image.open("logo.png")
        logo_img = CTkImage(dark_image=logo_img_data, light_image=logo_img_data, size=(52.71, 49.51))

        CTkLabel(master=sidebar_frame, text="", image=logo_img).pack(pady=(38, 0), anchor="center")

        self.sidebar_create_order_btn = CTkButton(master=sidebar_frame, text="Create Ticket", fg_color="transparent", font=("Arial Bold", 14), hover_color="#204B6B", anchor="w", command=lambda: self.switch_main_view("CREATE_ORDER"))

        self.sidebar_all_orders_btn = CTkButton(master=sidebar_frame, text="All Tickets", fg_color="transparent", font=("Arial Bold", 14), hover_color="#204B6B", anchor="w", command=lambda: self.switch_main_view("ALL_TICKETS"))

        self.sidebar_login_btn = CTkButton(master=sidebar_frame, text="Login", fg_color="transparent", font=("Arial Bold", 14), hover_color="#204B6B", anchor="w", command=lambda: self.switch_main_view("LOGIN"))
 

    def clear_main_view(self):
        for child in self.main_view.winfo_children():
            child.destroy()

    def switch_main_view(self, view):
        self.view = view
        self.clear_main_view()

        for btn in [self.sidebar_all_orders_btn, self.sidebar_create_order_btn, self.sidebar_login_btn]:
            btn.configure(fg_color="transparent")

        if self.view == "CREATE_ORDER":
            self.build_create_order_ui()
            self.sidebar_create_order_btn.configure(fg_color="#204B6B")

            self.sidebar_login_btn.pack_forget()
            self.sidebar_create_order_btn.pack(anchor="center", ipady=5, pady=(30, 0))
            self.sidebar_all_orders_btn.pack(anchor="center", ipady=5, pady=(15, 0))

        elif self.view == "ALL_TICKETS":
            self.build_all_tickets_ui()
            self.sidebar_all_orders_btn.configure(fg_color="#204B6B")

            self.sidebar_login_btn.pack_forget()
            self.sidebar_create_order_btn.pack(anchor="center", ipady=5, pady=(30, 0))
            self.sidebar_all_orders_btn.pack(anchor="center", ipady=5, pady=(15, 0))

        elif self.view == "LOGIN":
            self.build_login_ui()
            self.sidebar_login_btn.configure(fg_color="#204B6B")

            self.sidebar_login_btn.pack(anchor="center", ipady=5, pady=(15, 0))
            self.sidebar_create_order_btn.pack_forget()
            self.sidebar_all_orders_btn.pack_forget()
                
    def create_order(self):
        url = "https://firestore.googleapis.com/v1/projects/pavapp1-d8599/databases/(default)/documents/tickets"

        headers = {
            "Authorization": f"Bearer {self.token}"
        }

        input_data = {
            "fields": {
                "item_name": {
                    "stringValue": self.item_name.get()
                },
                "customer": {
                    "stringValue": self.customer.get()
                },
                "address": {
                    "stringValue": self.address.get()
                },
                "status": {
                    "stringValue": self.status_var.get()
                },
                "quantity": {
                    "integerValue": self.quantity
                }
            }
        }

        response = requests.post(url, json=input_data, headers=headers)
        response_data = response.json()

        if response.status_code == 200:
            CTkMessagebox(title="Success", message="Order created successfully", icon="check")
        else:
            error_message = response_data["error"]["message"]
            CTkMessagebox(title="Error", message=error_message, icon="cancel")

    def build_create_order_ui(self):
        CTkLabel(master=self.main_view, text="Create Ticket", font=("Arial Black", 25), text_color="#fff").pack(anchor="nw", pady=(29,0), padx=27)

        CTkLabel(master=self.main_view, text="Id", font=("Arial Bold", 17), text_color="#fff").pack(anchor="nw", pady=(25,0), padx=27)

        self.item_name = CTkEntry(master=self.main_view, fg_color="#F0F0F0", text_color="#000", border_width=0)
        self.item_name.pack(fill="x", pady=(12,0), padx=27, ipady=10)

        grid = CTkFrame(master=self.main_view, fg_color="transparent")
        grid.pack(fill="both", padx=27, pady=(31,0))

        CTkLabel(master=grid, text="Client", font=("Arial Bold", 17), text_color="#fff", justify="left").grid(row=0, column=0, sticky="w")
        self.customer = CTkEntry(master=grid, fg_color="#F0F0F0", text_color="#000", border_width=0, width=250)
        self.customer.grid(row=1, column=0, ipady=10)

        CTkLabel(master=grid, text="Description", font=("Arial Bold", 17), text_color="#fff", justify="left").grid(row=0, column=1, sticky="w", padx=(25,0))
        self.address = CTkEntry(master=grid, fg_color="#F0F0F0", text_color="#000", border_width=0, width=250)
        self.address.grid(row=1, column=1, ipady=10, sticky='w', padx=(25,0))

        CTkLabel(master=grid, text="Status", font=("Arial Bold", 17), text_color="#fff", justify="left").grid(row=2, column=0, sticky="w", pady=(38, 0))

        self.status_var = tkinter.StringVar(value="Ready")

        CTkRadioButton(master=grid, variable=self.status_var, value="Ready", text="Ready", font=("Arial Bold", 14), text_color="#fff", fg_color="#fff", border_color="#fff", hover_color="#F49A44").grid(row=3, column=0, sticky="w", pady=(16,0))
        CTkRadioButton(master=grid, variable=self.status_var, value="In progress", text="In progress", font=("Arial Bold", 14), text_color="#fff", fg_color="#fff", border_color="#fff", hover_color="#F49A44").grid(row=4, column=0, sticky="w", pady=(16,0))
        CTkRadioButton(master=grid, variable=self.status_var, value="Done", text="Done", font=("Arial Bold", 14), text_color="#fff", fg_color="#fff", border_color="#fff", hover_color="#F49A44").grid(row=5, column=0, sticky="w", pady=(16,0))

        CTkLabel(master=grid, text="Quantity", font=("Arial Bold", 17), text_color="#fff", justify="left").grid(row=2, column=1, sticky="w", pady=(20, 0), padx=(25,0))

        self.quantity = 1

        quantity_frame = CTkFrame(master=grid, fg_color="transparent")
        quantity_frame.grid(row=3, column=1, pady=(10,0), padx=(25,0), sticky="w")
        CTkButton(master=quantity_frame, text="-", width=25, text_color="#B0510C", fg_color="#fff", hover_color="#d6d6d6", font=("Arial Black", 16), command=lambda: self.update_quantity(self.quantity-1)).pack(side="left", anchor="w")
        self.quantity_label = CTkLabel(master=quantity_frame, text="01", text_color="#fff", font=("Arial Black", 16))
        self.quantity_label.pack(side="left", anchor="w", padx=10)
        CTkButton(master=quantity_frame, text="+", width=25, text_color="#B0510C", fg_color="#fff", hover_color="#d6d6d6", font=("Arial Black", 16),  command=lambda: self.update_quantity(self.quantity+1)).pack(side="left", anchor="w")

        CTkButton(master=self.main_view, text="Create", width=300, font=("Arial Bold", 17), hover_color="#B0510C", fg_color="#EE6B06", text_color="#fff", command=self.create_order).pack(fill="both", side="bottom", pady=(0, 25), ipady=10, padx=(27,27))

    def update_quantity(self, new_quantity):
        if new_quantity < 1:
            return

        self.quantity = new_quantity
        self.quantity_label.configure(text=str(self.quantity).zfill(2))

    def query_all_tickets(self):
        url = "https://firestore.googleapis.com/v1/projects/pavapp1-d8599/databases/(default)/documents/tickets"

        params = {
            "mask.fieldPaths": ["id", "client", "description", "Status", "Time"]
        }

        headers = {
            "Authorization": f"Bearer {self.token}"
        }

        response = requests.get(url, params=params, headers=headers)
        response_data = response.json()

        table_data = [
            ["ID", "Client", "Description", "Status", "Time"],
            # ["MacBook Pro", "John Doe", "123 Main St", "Shipped", "1"],
            # ["Galaxy S21", "Jane Smith", "456 Park Ave", "Delivered", "2"],
            # ["PlayStation 5", "Bob Johnson", "789 Broadway", "Processing", "1"],
        ]

        for doc in response_data["documents"]:
            row = []
            if "fields" in doc:
                fields = doc["fields"]
                row.append(fields["id"]["integerValue"])
                row.append(fields["client"]["stringValue"])
                row.append(fields["description"]["stringValue"])
                row.append(fields["Status"]["stringValue"])
                row.append(fields["Time"]["timestampValue"])
            
                table_data.append(row)
        
        return table_data
    
    def build_all_tickets_ui(self):
        table_data = self.query_all_tickets()
        
        CTkLabel(master=self.main_view, text="All Tickets", font=("Arial Black", 25), text_color="#fff").pack(anchor="nw", pady=(29,0), padx=27)

        table_frame = CTkScrollableFrame(master=self.main_view, fg_color="transparent")
        table_frame.pack(expand=True, fill="both", padx=27, pady=21)

        table = CTkTable(master=table_frame, column=5, values=table_data, font=("Arial", 11), text_color="#000", header_color="#F6830D", colors=["#FFCD32", "#f8b907"])
        table.pack(expand=True)

     
    def login_handler(self):
        input_data = {
            "username": self.username.get(),
            "email": self.email.get(),
            "password": self.password.get(),
            #"returnSecureToken": True
        }

        response = requests.post("http://127.0.0.1:8000/api/users/", 
                                  json=input_data)

        response_data = response.json()

        if response.status_code == 201:
            #self.token = response_data["idToken"]
            self.switch_main_view("CREATE_ORDER")
            CTkMessagebox(icon="check", message="Login successful")
        else:
            error_message = response_data["error"]["message"]
            CTkMessagebox(icon="cancel", message=error_message)

    def build_login_ui(self):
       CTkLabel(master=self.main_view, text="Login", font=("Arial Black", 25), text_color="#fff").pack(anchor="nw", pady=(29,0), padx=27)
       
       CTkLabel(master=self.main_view, text="Email", font=("Arial Bold", 17), text_color="#fff").pack(anchor="nw", pady=(25,0), padx=27)

       self.email = CTkEntry(master=self.main_view, fg_color="#F0F0F0", text_color="#000", border_width=0)
       self.email.pack(fill="x", pady=(12,0), padx=27, ipady=10)

       CTkLabel(master=self.main_view, text="Username", font=("Arial Bold", 17), text_color="#fff").pack(anchor="nw", pady=(25,0), padx=27)

       self.username = CTkEntry(master=self.main_view, fg_color="#F0F0F0", text_color="#000", border_width=0)
       self.username.pack(fill="x", pady=(12,0), padx=27, ipady=10)

       CTkLabel(master=self.main_view, text="Password", font=("Arial Bold", 17), text_color="#fff").pack(anchor="nw", pady=(25,0), padx=27)

       self.password = CTkEntry(master=self.main_view, fg_color="#F0F0F0", text_color="#000", border_width=0, show="*")
       self.password.pack(fill="x", pady=(12,0), padx=27, ipady=10)

       self.show_password_var = BooleanVar()
       self.password_show_check = CTkCheckBox(master=self.main_view, text="Показать пароль", variable=self.show_password_var, command=self.toggle_password_visibility, checkbox_height= 20, checkbox_width= 20)
       self.password_show_check.pack(fill="x", pady=(12,0), padx=27, ipady=10)
       
       CTkButton(master=self.main_view, text="Login", width=300, font=("Arial Bold", 17), hover_color="#B0510C", fg_color="#EE6B06", text_color="#fff", command=self.login_handler).pack(fill="both", side="bottom", pady=(0, 50), ipady=10, padx=(27,27))

    def toggle_password_visibility(self):
        if self.show_password_var.get():
            self.password.configure(show="")
        else:
            self.password.configure(show="*")
    
if __name__ == "__main__":
    app = App()
    app.mainloop()