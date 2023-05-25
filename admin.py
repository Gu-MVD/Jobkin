import customtkinter as ctk
from tkinter import ttk
from connection import Connection


class TabView(ctk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Подключение к БД
        global connection
        try:
            connection = Connection()
            connection.open()
        except Exception as e:
            print(e)

        # Таблица student
        # Заполнение заголовков таблицы
        columns = connection.get_columns()
        self.studentsTab = self.add("students")
        self.tree = ttk.Treeview(master=self.studentsTab, columns=columns, show="headings")
        self.tree.pack(fill="both", expand=1, padx=20, pady=10)
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("Treeview", fieldbackground="#2B2B2B", background="#2B2B2B", foreground="#FFFFFF",
                        relief='flat', borderwidth=0)
        style.configure("Treeview.Heading", fieldbackground="#2FA572", background="#2FA572", foreground="#242424",
                        relief='flat', borderwidth=0)

        for column in columns:
            self.tree.heading(column, text=column, anchor="w")

        self.tree.column("#1", stretch=False, width=40)
        self.tree.column("#2", stretch=False, width=120)
        self.tree.column("#3", stretch=False, width=120)
        self.tree.column("#4", stretch=False, width=120)
        self.tree.column("#5", stretch=False, width=120)

        # Заполнение таблицы данными
        rows = connection.get_rows()
        for row in rows:
            self.tree.insert("", "end", values=list(row.values()))

        # Поля для обновления данных
        self.tree.bind("<<TreeviewSelect>>", self.get_selection)

        self.frame = ctk.CTkFrame(self.studentsTab)
        self.idEntry = ctk.CTkEntry(self.frame, placeholder_text="ID", width=50)
        self.nameEntry = ctk.CTkEntry(self.frame, placeholder_text="STUDENTNAME")
        self.dateEntry = ctk.CTkEntry(self.frame, placeholder_text="DATEOFBIRTH")
        self.groupEntry = ctk.CTkEntry(self.frame, placeholder_text="GROUPNUMBER")
        self.spEntry = ctk.CTkEntry(self.frame, placeholder_text="SPECIALTYCODE")
        self.telEntry = ctk.CTkEntry(self.frame, placeholder_text="TELEPHONENUMBER")
        self.emailEntry = ctk.CTkEntry(self.frame, placeholder_text="EMAILADDRESS")
        self.frame.pack(padx=20, pady=10)
        self.idEntry.pack(side="left")
        self.nameEntry.pack(side="left")
        self.dateEntry.pack(side="left")
        self.groupEntry.pack(side="left")
        self.spEntry.pack(side="left")
        self.telEntry.pack(side="left")
        self.emailEntry.pack(side="left")

        self.refreshButton = ctk.CTkButton(self.studentsTab, text="refresh", command=self.refreshTable)
        self.updateButton = ctk.CTkButton(self.studentsTab, text="update", command=self.updateRow)
        self.deleteButton = ctk.CTkButton(self.studentsTab, text="delete", command=self.deleteRow)
        self.insertButton = ctk.CTkButton(self.studentsTab, text="insert", command=self.insertRow)
        self.refreshButton.pack(side="right", padx=(0, 44))
        self.updateButton.pack(side="right", padx=20)
        self.deleteButton.pack(side="right", padx=(20, 0))
        self.insertButton.pack(side="right", padx=(20, 0))

        self.additional_infoTab = self.add("student_additional_info")
        self.additional_info = ctk.CTkLabel(self.additional_infoTab, text="to be continued...",
                                            font=("Open Sans", 32, "bold"))
        self.additional_info.pack(anchor="center", fill="both", expand=1)

    def refreshTable(self):
        connection.select_student()
        self.tree.delete(*self.tree.get_children())
        rows = connection.get_rows()
        for row in rows:
            self.tree.insert("", "end", values=list(row.values()))

    def updateRow(self):
        connection.update_student(self.idEntry.get(), self.nameEntry.get(), self.dateEntry.get(),
                                  self.groupEntry.get(), self.spEntry.get(), self.telEntry.get(), self.emailEntry.get())
        self.refreshTable()
        self.clearEntry()

    def deleteRow(self):
        connection.delete_from_student(self.idEntry.get())
        self.refreshTable()
        self.clearEntry()

    def insertRow(self):
        connection.insert_into_student(self.nameEntry.get(), self.dateEntry.get(),self.groupEntry.get(),
                                       self.spEntry.get(), self.telEntry.get(), self.emailEntry.get())
        self.refreshTable()
        self.clearEntry()

    def get_selection(self, event):
        self.clearEntry()
        for selection in self.tree.selection():
            item = self.tree.item(selection)
            id, name, date, group, sp, tel, email = item["values"][0:7]
            self.idEntry.insert(0, id)
            self.nameEntry.insert(0, name)
            self.dateEntry.insert(0, date)
            self.groupEntry.insert(0, group)
            self.spEntry.insert(0, sp)
            self.telEntry.insert(0, tel)
            self.emailEntry.insert(0, email)

    def clearEntry(self):
        self.idEntry.delete(0, "end")
        self.nameEntry.delete(0, "end")
        self.dateEntry.delete(0, "end")
        self.groupEntry.delete(0, "end")
        self.spEntry.delete(0, "end")
        self.telEntry.delete(0, "end")
        self.emailEntry.delete(0, "end")


class AdminWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("1000x800")

        self.title("Jobkin")

        self.tab_view = TabView(master=self)
        self.tab_view.pack(expand=1, fill="both", padx=30, pady=30)
