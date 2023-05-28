import customtkinter as ctk
from login import LoginApp

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")

app = LoginApp()
try:
    app.mainloop()
except KeyboardInterrupt:
    print("Программа завершена")

