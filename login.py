import customtkinter as ctk
import utility
from admin import AdminWindow


class LoginApp(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Authorization")
        self.geometry("320x175+800+375")

        self.grid_columnconfigure(1, weight=1)

        self.windowTitle = ctk.CTkLabel(self, text="Login", font=("Open Sans", 32, "bold"))
        self.windowTitle.grid(row=0, column=1, pady=10)

        self.loginField = ctk.CTkEntry(self, placeholder_text="login", corner_radius=12)
        self.loginField.grid(row=1, column=0, columnspan=3, sticky="ew", padx=10)
        self.passwordField = ctk.CTkEntry(self, placeholder_text="password", corner_radius=12, show="\u2022")
        self.passwordField.grid(row=2, column=0, columnspan=3, sticky="ew", padx=10, pady=10)

        self.loginButton = ctk.CTkButton(self, text="Login", corner_radius=12, command=self.login)
        self.loginButton.grid(row=3, column=1)

        self.topLevelWindow = None

    def login(self):
        if utility.verify(self.loginField.get(), self.passwordField.get()):
            if self.topLevelWindow is None or not self.topLevelWindow.winfo_exists():
                self.topLevelWindow = AdminWindow(self)
                self.withdraw()
            else:
                self.topLevelWindow.focus()
