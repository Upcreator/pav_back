from customtkinter import *
from PIL import Image
import tkinter
import requests
from CTkTable import CTkTable
from CTkMessagebox import CTkMessagebox

from datetime import datetime
class App(CTk):
    app_width = 750
    app_height = 550
    def __init__(self, **kw):
        super().__init__( **kw)
        self.geometry(f"{self.app_width}x{self.app_height}")
        #self.geometry("750x550")
        self.title("PavApp")
        self.resizable(0,0)
        set_appearance_mode("dark")
        self.center_window()

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

        self.sidebar_create_order_btn = CTkButton(master=sidebar_frame, text="Создать Заявку", fg_color="transparent", font=("Arial Bold", 14), hover_color="#204B6B", anchor="w", command=lambda: self.switch_main_view("CREATE_ORDER"))

        self.sidebar_all_orders_btn = CTkButton(master=sidebar_frame, text="Все Заявки", fg_color="transparent", font=("Arial Bold", 14), hover_color="#204B6B", anchor="w", command=lambda: self.switch_main_view("ALL_TICKETS"))

        self.sidebar_login_btn = CTkButton(master=sidebar_frame, text="Логин", fg_color="transparent", font=("Arial Bold", 14), hover_color="#204B6B", anchor="w", command=lambda: self.switch_main_view("LOGIN"))
 
        self.sidebar_license_btn = CTkButton(master=sidebar_frame, text="Лицензия", fg_color="transparent", font=("Arial Bold", 14), hover_color="#204B6B", anchor="w", command=lambda: self.switch_main_view("LICENSE"))
        
        self.appearance_mode_optionemenu = CTkOptionMenu(master=sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
    def clear_main_view(self):
        for child in self.main_view.winfo_children():
            child.destroy()

    def switch_main_view(self, view):
        self.view = view
        self.clear_main_view()

        for btn in [self.sidebar_all_orders_btn, self.sidebar_create_order_btn, self.sidebar_login_btn, self.sidebar_license_btn]:
            btn.configure(fg_color="transparent")

        if self.view == "CREATE_ORDER":
            self.build_create_order_ui()
            self.sidebar_create_order_btn.configure(fg_color="#204B6B")

            self.sidebar_login_btn.pack_forget()
            self.sidebar_create_order_btn.pack(anchor="center", ipady=5, pady=(30, 0))
            self.sidebar_all_orders_btn.pack(anchor="center", ipady=5, pady=(15, 0))
            self.sidebar_license_btn.pack(anchor="center", ipady=5, pady=(15, 0))
            self.appearance_mode_optionemenu.pack(anchor="center", ipady=5, pady=(15, 0))
            

        elif self.view == "ALL_TICKETS":
            self.build_all_tickets_ui()
            self.sidebar_all_orders_btn.configure(fg_color="#204B6B")

            self.sidebar_login_btn.pack_forget()
            self.sidebar_create_order_btn.pack(anchor="center", ipady=5, pady=(30, 0))
            self.sidebar_all_orders_btn.pack(anchor="center", ipady=5, pady=(15, 0))
            self.sidebar_license_btn.pack(anchor="center", ipady=5, pady=(15, 0))


        elif self.view == "LOGIN":
            self.build_login_ui()
            self.sidebar_login_btn.configure(fg_color="#204B6B")

            self.sidebar_login_btn.pack(anchor="center", ipady=5, pady=(15, 0))
            self.sidebar_create_order_btn.pack_forget()
            self.sidebar_all_orders_btn.pack_forget()

        elif self.view == "LICENSE":
            self.build_license_activate_ui()
            self.sidebar_license_btn.configure(fg_color="#204B6B")

            self.sidebar_login_btn.pack_forget()
            self.sidebar_create_order_btn.pack(anchor="center", ipady=5, pady=(30, 0))
            self.sidebar_all_orders_btn.pack(anchor="center", ipady=5, pady=(15, 0))
            self.sidebar_license_btn.pack(anchor="center", ipady=5, pady=(15, 0))
                
    def create_order(self):
        url = "http://127.0.0.1:8000/api/tickets/"

        headers = {
            "Authorization": f"Bearer {self.access_token}"
        }

        input_data = {
            "ticket_number": self.ticket_number.get(),
            "client": self.client.get(),
            "problem_description": self.description.get(),
            "status": self.status_var.get(),
            
        }

        response = requests.post(url, json=input_data, headers=headers)
        response_data = response.json()
        
        print(response_data)
        if response.status_code == 201:
            CTkMessagebox(title="Успешно", message="Заявка создана успешно", icon="check")
        else:
            error_message = response_data["error"]["message"]
            CTkMessagebox(title="Error", message=error_message, icon="cancel")
            

    def build_create_order_ui(self):
        CTkLabel(master=self.main_view, text="Создать заявку", font=("Arial Black", 25), text_color="#fff").pack(anchor="nw", pady=(29,0), padx=27)

        CTkLabel(master=self.main_view, text="Номер заявки", font=("Arial Bold", 17), text_color="#fff").pack(anchor="nw", pady=(25,0), padx=27)

        self.ticket_number = CTkEntry(master=self.main_view, fg_color="#F0F0F0", text_color="#000", border_width=0)
        self.ticket_number.pack(fill="x", pady=(12,0), padx=27, ipady=10)

        grid = CTkFrame(master=self.main_view, fg_color="transparent")
        grid.pack(fill="both", padx=27, pady=(31,0))

        CTkLabel(master=grid, text="Клиент", font=("Arial Bold", 17), text_color="#fff", justify="left").grid(row=0, column=0, sticky="w")
        self.client = CTkEntry(master=grid, fg_color="#F0F0F0", text_color="#000", border_width=0, width=250)
        self.client.grid(row=1, column=0, ipady=10)

        CTkLabel(master=grid, text="Описание", font=("Arial Bold", 17), text_color="#fff", justify="left").grid(row=0, column=1, sticky="w", padx=(25,0))
        self.description = CTkEntry(master=grid, fg_color="#F0F0F0", text_color="#000", border_width=0, width=250)
        self.description.grid(row=1, column=1, ipady=10, sticky='w', padx=(25,0))

        CTkLabel(master=grid, text="Статус", font=("Arial Bold", 17), text_color="#fff", justify="left").grid(row=2, column=0, sticky="w", pady=(38, 0))

        self.status_var = tkinter.StringVar(value="В ожидании")

        CTkRadioButton(master=grid, variable=self.status_var, value="В ожидании", text="В ожидании", font=("Arial Bold", 14), text_color="#fff", fg_color="#fff", border_color="#fff", hover_color="#F49A44").grid(row=3, column=0, sticky="w", pady=(16,0))
        CTkRadioButton(master=grid, variable=self.status_var, value="В работе", text="В работе", font=("Arial Bold", 14), text_color="#fff", fg_color="#fff", border_color="#fff", hover_color="#F49A44").grid(row=4, column=0, sticky="w", pady=(16,0))
        CTkRadioButton(master=grid, variable=self.status_var, value="Выполнено", text="Выполнено", font=("Arial Bold", 14), text_color="#fff", fg_color="#fff", border_color="#fff", hover_color="#F49A44").grid(row=5, column=0, sticky="w", pady=(16,0))

        CTkLabel(master=grid, text="Тип проблемы", font=("Arial Bold", 17), text_color="#fff", justify="left").grid(row=2, column=1, sticky="w", pady=(38, 0))

        self.fault_type_var = tkinter.StringVar(value="Комп не работает")

        CTkRadioButton(master=grid, variable=self.status_var, value="Комп не работает", text="Комп не работает", font=("Arial Bold", 14), text_color="#fff", fg_color="#fff", border_color="#fff", hover_color="#F49A44").grid(row=3, column=1, sticky="w", pady=(16,0))
        CTkRadioButton(master=grid, variable=self.status_var, value="Wi-fi глючит", text="Wi-fi глючит", font=("Arial Bold", 14), text_color="#fff", fg_color="#fff", border_color="#fff", hover_color="#F49A44").grid(row=4, column=1, sticky="w", pady=(16,0))
        CTkRadioButton(master=grid, variable=self.status_var, value="Excel залагал", text="Excel залагал", font=("Arial Bold", 14), text_color="#fff", fg_color="#fff", border_color="#fff", hover_color="#F49A44").grid(row=5, column=1, sticky="w", pady=(16,0))
        """CTkLabel(master=grid, text="Надо убрать", font=("Arial Bold", 17), text_color="#fff", justify="left").grid(row=2, column=1, sticky="w", pady=(20, 0), padx=(25,0))

        self.quantity = 1

        quantity_frame = CTkFrame(master=grid, fg_color="transparent")
        quantity_frame.grid(row=3, column=1, pady=(10,0), padx=(25,0), sticky="w")
        CTkButton(master=quantity_frame, text="-", width=25, text_color="#B0510C", fg_color="#fff", hover_color="#d6d6d6", font=("Arial Black", 16), command=lambda: self.update_quantity(self.quantity-1)).pack(side="left", anchor="w")
        self.quantity_label = CTkLabel(master=quantity_frame, text="01", text_color="#fff", font=("Arial Black", 16))
        self.quantity_label.pack(side="left", anchor="w", padx=10)
        CTkButton(master=quantity_frame, text="+", width=25, text_color="#B0510C", fg_color="#fff", hover_color="#d6d6d6", font=("Arial Black", 16),  command=lambda: self.update_quantity(self.quantity+1)).pack(side="left", anchor="w")"""

        CTkButton(master=self.main_view, text="Создать", width=300, font=("Arial Bold", 17), hover_color="#B0510C", fg_color="#EE6B06", text_color="#fff", command=self.create_order).pack(fill="both", side="bottom", pady=(0, 25), ipady=10, padx=(27,27))

    def build_license_activate_ui(self):
        CTkLabel(master=self.main_view, text="Активация Лицензии", font=("Arial Black", 25), text_color="#fff").pack(anchor="nw", pady=(29,0), padx=27)

        CTkLabel(master=self.main_view, text="Введите лицензионный ключ", font=("Arial Bold", 17), text_color="#fff").pack(anchor="nw", pady=(25,0), padx=27)

        self.license_key = CTkEntry(master=self.main_view, fg_color="#F0F0F0", text_color="#000", border_width=0)
        self.license_key.pack(fill="x", pady=(12,0), padx=27, ipady=10)

        CTkButton(master=self.main_view, text="Активировать", width=300, font=("Arial Bold", 17), hover_color="#B0510C", fg_color="#EE6B06", text_color="#fff", command=self.activate_license).pack(fill="both", side="bottom", pady=(0, 25), ipady=10, padx=(27,27))
    
    def change_appearance_mode_event(self, new_appearance_mode: str):
        set_appearance_mode(new_appearance_mode)

    def activate_license(self):
        license_key_value = self.license_key.get()
        url = f"http://127.0.0.1:8000/api/licenses/{license_key_value}/activate/"

        headers = {
            "Authorization": f"Bearer {self.access_token}"
        }

        input_data = {
            #"key": self.license_key.get(),
        }

        response = requests.patch(url, json=input_data, headers=headers)
        response_data = response.json()
        
        print(response_data)
        if response.status_code == 200:
            CTkMessagebox(title="Успешно", message="Лицензия активирована!", icon="check")
            self.license_key.delete(0, 'end')
        else:
            error_message = response_data["error"]["message"]
            CTkMessagebox(title="Error", message=error_message, icon="cancel")

    def update_quantity(self, new_quantity):
        if new_quantity < 1:
            return

        self.quantity = new_quantity
        self.quantity_label.configure(text=str(self.quantity).zfill(2))

    def query_all_tickets(self):
        url = "http://127.0.0.1:8000/api/tickets/"

        params = {
            "mask.fieldPaths": ["ticket_number", "client", "description", "status", "created_at"]
        }

        headers = {
            "Authorization": f"Bearer {self.access_token}"
        }

        response = requests.get(url, params=params, headers=headers)
        response_data = response.json()

        table_data = [
            ["Номер", "Клиент", "Описание", "Статус", "Время создания"],
            # ["MacBook Pro", "John Doe", "123 Main St", "Shipped", "1"],
            # ["Galaxy S21", "Jane Smith", "456 Park Ave", "Delivered", "2"],
            # ["PlayStation 5", "Bob Johnson", "789 Broadway", "Processing", "1"],
        ]

        """for doc in response_data["documents"]:
            row = []
            if "fields" in doc:
                fields = doc["fields"]
                row.append(fields["ticket_number"]["stringValue"])
                row.append(fields["client"]["stringValue"])
                row.append(fields["description"]["stringValue"])
                row.append(fields["status"]["stringValue"])
                row.append(fields["created_at"]["timestampValue"])
            
                table_data.append(row)"""
        if isinstance(response_data, list):
            for doc in response_data:
                row = []
                row.append(doc.get("ticket_number", ""))
                row.append(doc.get("client", ""))
                row.append(doc.get("problem_description", ""))
                row.append(doc.get("status", ""))
                created_at = doc.get("created_at", "")
                if created_at:
                    created_at = datetime.strptime(created_at, '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%Y-%m-%d %H:%M:%S')
                row.append(created_at)
                table_data.append(row)
        return table_data
    
    def build_all_tickets_ui(self):
        table_data = self.query_all_tickets()
        
        CTkLabel(master=self.main_view, text="Все заявки", font=("Arial Black", 25), text_color="#fff").pack(anchor="nw", pady=(29,0), padx=27)

        table_frame = CTkScrollableFrame(master=self.main_view, fg_color="transparent")
        table_frame.pack(expand=True, fill="both", padx=27, pady=21)

        table = CTkTable(master=table_frame, column=5, values=table_data, font=("Arial", 11), text_color="#000", header_color="#F6830D", colors=["#FFCD32", "#f8b907"])
        table.pack(expand=True)

     
    def login_handler(self):
        input_data = {
            "username": self.username.get(),
            #"email": self.email.get(),
            "password": self.password.get(),
            #"returnSecureToken": True
        }

        response = requests.post("http://127.0.0.1:8000/api/token/", 
                                  json=input_data)

        response_data = response.json()

        if response.status_code == 200:
            self.access_token = response_data["access"]
            self.refresh_token = response_data["refresh"]
            self.switch_main_view("CREATE_ORDER")
            CTkMessagebox(icon="check", message="Авторизация успешна")
        else:
            CTkMessagebox(icon="cancel", message="Неверный логин или пароль")
            #error_message = response_data["error"]["message"]
            #CTkMessagebox(icon="cancel", message=error_message)

    def build_login_ui(self):
       CTkLabel(master=self.main_view, text="Логин", font=("Arial Black", 25), text_color="#fff").pack(anchor="nw", pady=(29,0), padx=27)

       CTkLabel(master=self.main_view, text="Логин", font=("Arial Bold", 17), text_color="#fff").pack(anchor="nw", pady=(25,0), padx=27)

       self.username = CTkEntry(master=self.main_view, fg_color="#F0F0F0", text_color="#000", border_width=0)
       self.username.pack(fill="x", pady=(12,0), padx=27, ipady=10)

       CTkLabel(master=self.main_view, text="Пароль", font=("Arial Bold", 17), text_color="#fff").pack(anchor="nw", pady=(25,0), padx=27)

       self.password = CTkEntry(master=self.main_view, fg_color="#F0F0F0", text_color="#000", border_width=0, show="*")
       self.password.pack(fill="x", pady=(12,0), padx=27, ipady=10)

       self.show_password_var = BooleanVar()
       self.password_show_check = CTkCheckBox(master=self.main_view, text="Показать пароль", variable=self.show_password_var, command=self.toggle_password_visibility, checkbox_height= 20, checkbox_width= 20)
       self.password_show_check.pack(fill="x", pady=(12,0), padx=27, ipady=10)
       
       CTkButton(master=self.main_view, text="Войти", width=300, font=("Arial Bold", 17), hover_color="#B0510C", fg_color="#EE6B06", text_color="#fff", command=self.login_handler).pack(fill="both", side="bottom", pady=(0, 50), ipady=10, padx=(27,27))

    def toggle_password_visibility(self):
        if self.show_password_var.get():
            self.password.configure(show="")
        else:
            self.password.configure(show="*")
    
    def center_window(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_position = (screen_width - self.app_width) // 2
        y_position = (screen_height - self.app_height) // 2

        self.geometry(f"{self.app_width}x{self.app_height}+{x_position}+{y_position}")
    
if __name__ == "__main__":
    app = App()
    app.mainloop()