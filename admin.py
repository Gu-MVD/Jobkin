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
        columns = connection.get_columns(connection.select_student())
        self.studentsTab = self.add("students")
        self.tree_student = ttk.Treeview(master=self.studentsTab, columns=columns, show="headings")
        self.tree_student.pack(fill="both", expand=1, padx=20, pady=10)
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("Treeview", fieldbackground="#2B2B2B", background="#2B2B2B", foreground="#FFFFFF",
                        relief='flat', borderwidth=0)
        style.configure("Treeview.Heading", fieldbackground="#2FA572", background="#2FA572", foreground="#242424",
                        relief='flat', borderwidth=0)

        for column in columns:
            self.tree_student.heading(column, text=column, anchor="w")

        self.tree_student.column("#1", stretch=False, width=40)
        self.tree_student.column("#2", stretch=False, width=120)
        self.tree_student.column("#3", stretch=False, width=120)
        self.tree_student.column("#4", stretch=False, width=120)
        self.tree_student.column("#5", stretch=False, width=120)

        # Заполнение таблицы данными
        rows = connection.get_rows(connection.select_student())
        for row in rows:
            self.tree_student.insert("", "end", values=list(row.values()))

        # Поля для обновления данных
        self.tree_student.bind("<<TreeviewSelect>>", self.get_selection_student)

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

        # Кнопки для действий с таблицей
        self.refreshButton = ctk.CTkButton(self.studentsTab, text="refresh", command=self.refreshTable_student)
        self.updateButton = ctk.CTkButton(self.studentsTab, text="update", command=self.updateRow_student)
        self.deleteButton = ctk.CTkButton(self.studentsTab, text="delete", command=self.deleteRow_student)
        self.insertButton = ctk.CTkButton(self.studentsTab, text="insert", command=self.insertRow_student)
        self.refreshButton.pack(side="right", padx=(0, 44))
        self.updateButton.pack(side="right", padx=20)
        self.deleteButton.pack(side="right", padx=(20, 0))
        self.insertButton.pack(side="right", padx=(20, 0))

        # Таблица student_additional_info
        # Заполнение заголовков таблицы
        columns = connection.get_columns(connection.select_student_additional_info())
        self.additional_infoTab = self.add("student_additional_info")
        self.tree_student_additional_info = ttk.Treeview(master=self.additional_infoTab, columns=columns,
                                                         show="headings")
        self.tree_student_additional_info.pack(fill="both", expand=1, padx=20, pady=10)

        for column in columns:
            self.tree_student_additional_info.heading(column, text=column, anchor="w")

        self.tree_student_additional_info.column("#1", stretch=False, width=200)
        self.tree_student_additional_info.column("#2", stretch=False, width=120)
        self.tree_student_additional_info.column("#3", stretch=False, width=90)
        self.tree_student_additional_info.column("#4", stretch=False, width=200)
        self.tree_student_additional_info.column("#5", stretch=False, width=110)

        # Заполнение таблицы данными
        rows = connection.get_rows(connection.select_student_additional_info())
        for row in rows:
            self.tree_student_additional_info.insert("", "end", values=list(row.values()))

        # Поля для обновления данных
        self.tree_student_additional_info.bind("<<TreeviewSelect>>", self.get_selection_student_additional_info)

        self.frame_student_additional_info = ctk.CTkFrame(self.additional_infoTab)
        self.add_info_add_infoEntry = ctk.CTkEntry(self.frame_student_additional_info,
                                                   placeholder_text="ADDITIONALINFO")
        self.foreign_language_add_infoEntry = ctk.CTkEntry(self.frame_student_additional_info,
                                                           placeholder_text="FOREIGNLANGUAGE")
        self.driver_license_add_infoEntry = ctk.CTkEntry(self.frame_student_additional_info,
                                                         placeholder_text="DRIVERLICENSE")
        self.add_competencies_add_infoEntry = ctk.CTkEntry(self.frame_student_additional_info,
                                                           placeholder_text="ADDITIONALCOMPETENCIES")
        self.social_network_add_infoEntry = ctk.CTkEntry(self.frame_student_additional_info,
                                                         placeholder_text="SOCIALNETWORK")
        self.id_add_infoEntry = ctk.CTkEntry(self.frame_student_additional_info,
                                             placeholder_text="ID")
        self.frame_student_additional_info.pack(padx=20, pady=10)
        self.add_info_add_infoEntry.pack(side="left")
        self.foreign_language_add_infoEntry.pack(side="left")
        self.driver_license_add_infoEntry.pack(side="left")
        self.add_competencies_add_infoEntry.pack(side="left")
        self.social_network_add_infoEntry.pack(side="left")
        self.id_add_infoEntry.pack(side="left")

        # Кнопки для действий с таблицей
        # ...

        # Таблица student_soft_skills
        # Заполнение заголовков таблицы
        columns = connection.get_columns(connection.select_student_soft_skills())
        self.soft_skillsTab = self.add("student_soft_skills")
        self.tree_student_soft_skills = ttk.Treeview(master=self.soft_skillsTab, columns=columns,
                                                     show="headings")
        self.tree_student_soft_skills.pack(fill="both", expand=1, padx=20, pady=10)

        for column in columns:
            self.tree_student_soft_skills.heading(column, text=column, anchor="w")

        self.tree_student_soft_skills.column("#1", stretch=False, width=40)
        self.tree_student_soft_skills.column("#2", stretch=False, width=150)
        self.tree_student_soft_skills.column("#3", stretch=False, width=150)
        self.tree_student_soft_skills.column("#4", stretch=False, width=150)
        self.tree_student_soft_skills.column("#5", stretch=False, width=150)

        # Заполнение таблицы данными
        rows = connection.get_rows(connection.select_student_soft_skills())
        for row in rows:
            self.tree_student_soft_skills.insert("", "end", values=list(row.values()))

        # Поля для обновления данных
        # ...

        # Кнопки для действий с таблицей
        # ...

        # Таблица student_education
        # Заполнение заголовков таблицы
        columns = connection.get_columns(connection.select_student_education())
        self.educationTab = self.add("student_education")
        self.tree_student_education = ttk.Treeview(master=self.educationTab, columns=columns,
                                                   show="headings")
        self.tree_student_education.pack(fill="both", expand=1, padx=20, pady=10)

        for column in columns:
            self.tree_student_education.heading(column, text=column, anchor="w")

        self.tree_student_education.column("#1", stretch=False, width=40)
        self.tree_student_education.column("#2", stretch=False, width=150)
        self.tree_student_education.column("#3", stretch=False, width=150)
        self.tree_student_education.column("#4", stretch=False, width=150)
        self.tree_student_education.column("#5", stretch=False, width=150)

        # Заполнение таблицы данными
        rows = connection.get_rows(connection.select_student_education())
        for row in rows:
            self.tree_student_education.insert("", "end", values=list(row.values()))

        # Поля для обновления данных
        # ...

        # Кнопки для действий с таблицей
        # ...

        # Таблица student_competencies
        # Заполнение заголовков таблицы
        columns = connection.get_columns(connection.select_student_competencies())
        self.competenciesTab = self.add("student_competencies")
        self.tree_student_competencies = ttk.Treeview(master=self.competenciesTab, columns=columns,
                                                      show="headings")
        self.tree_student_competencies.pack(fill="both", expand=1, padx=20, pady=10)

        for column in columns:
            self.tree_student_competencies.heading(column, text=column, anchor="w")

        self.tree_student_competencies.column("#1", stretch=False, width=40)
        self.tree_student_competencies.column("#2", stretch=False, width=150)
        self.tree_student_competencies.column("#3", stretch=False, width=150)
        self.tree_student_competencies.column("#4", stretch=False, width=150)
        self.tree_student_competencies.column("#5", stretch=False, width=150)

        # Заполнение таблицы данными
        rows = connection.get_rows(connection.select_student_competencies())
        for row in rows:
            self.tree_student_competencies.insert("", "end", values=list(row.values()))

        # Поля для обновления данных
        # ...

        # Кнопки для действий с таблицей
        # ...

        # Таблица decoding_competency_full
        # Заполнение заголовков таблицы
        columns = connection.get_columns(connection.select_decoding_competency_full())
        self.decodingTab = self.add("decoding_competency_full")
        self.tree_decoding_competency = ttk.Treeview(master=self.decodingTab, columns=columns,
                                                     show="headings")
        self.tree_decoding_competency.pack(fill="both", expand=1, padx=20, pady=10)

        for column in columns:
            self.tree_decoding_competency.heading(column, text=column, anchor="w")

        self.tree_decoding_competency.column("#1", stretch=False, width=100)
        self.tree_decoding_competency.column("#2", stretch=False, width=150)
        self.tree_decoding_competency.column("#3", stretch=False, width=150)
        self.tree_decoding_competency.column("#4", stretch=False, width=150)
        self.tree_decoding_competency.column("#5", stretch=False, width=150)

        # Заполнение таблицы данными
        rows = connection.get_rows(connection.select_decoding_competency_full())
        for row in rows:
            self.tree_decoding_competency.insert("", "end", values=list(row.values()))

        # Поля для обновления данных
        # ...

        # Кнопки для действий с таблицей
        # ...

        # Таблица specialty_code
        # Заполнение заголовков таблицы
        columns = connection.get_columns(connection.select_specialty_code())
        self.specialtyTab = self.add("specialty_code")
        self.tree_specialty_code = ttk.Treeview(master=self.specialtyTab, columns=columns,
                                                show="headings")
        self.tree_specialty_code.pack(fill="both", expand=1, padx=20, pady=10)

        for column in columns:
            self.tree_specialty_code.heading(column, text=column, anchor="w")

        self.tree_specialty_code.column("#1", stretch=False, width=100)
        self.tree_specialty_code.column("#2", stretch=False, width=150)

        # Заполнение таблицы данными
        rows = connection.get_rows(connection.select_specialty_code())
        for row in rows:
            self.tree_specialty_code.insert("", "end", values=list(row.values()))

        # Поля для обновления данных
        # ...

        # Кнопки для действий с таблицей
        # ...

        # Таблица student_photo
        # Заполнение заголовков таблицы
        columns = connection.get_columns(connection.select_specialty_code())
        self.photoTab = self.add("student_photo")
        self.tree_student_photo = ttk.Treeview(master=self.photoTab, columns=columns,
                                               show="headings")
        self.tree_student_photo.pack(fill="both", expand=1, padx=20, pady=10)

        for column in columns:
            self.tree_student_photo.heading(column, text=column, anchor="w")

        self.tree_student_photo.column("#1", stretch=False, width=100)
        self.tree_student_photo.column("#2", stretch=False, width=150)

        # Заполнение таблицы данными
        rows = connection.get_rows(connection.select_student_photo())
        for row in rows:
            self.tree_student_photo.insert("", "end", values=list(row.values()))

        # Поля для обновления данных
        # ...

        # Кнопки для действий с таблицей
        # ...

    # Методы для таблицы student
    def refreshTable_student(self):
        # connection.select_student()
        self.tree_student.delete(*self.tree_student.get_children())
        rows = connection.get_rows(connection.select_student())
        for row in rows:
            self.tree_student.insert("", "end", values=list(row.values()))

    def updateRow_student(self):
        connection.update_student(self.idEntry.get(), self.nameEntry.get(), self.dateEntry.get(),
                                  self.groupEntry.get(), self.spEntry.get(), self.telEntry.get(), self.emailEntry.get())
        self.refreshTable_student()
        self.clearEntry_student()

    def deleteRow_student(self):
        connection.delete_from_student(self.idEntry.get())
        self.refreshTable_student()
        self.clearEntry_student()

    def insertRow_student(self):
        connection.insert_into_student(self.nameEntry.get(), self.dateEntry.get(), self.groupEntry.get(),
                                       self.spEntry.get(), self.telEntry.get(), self.emailEntry.get())
        self.refreshTable_student()
        self.clearEntry_student()

    def get_selection_student(self, event):
        self.clearEntry_student()
        for selection in self.tree_student.selection():
            item = self.tree_student.item(selection)
            id, name, date, group, sp, tel, email = item["values"][0:7]
            self.idEntry.insert(0, id)
            self.nameEntry.insert(0, name)
            self.dateEntry.insert(0, date)
            self.groupEntry.insert(0, group)
            self.spEntry.insert(0, sp)
            self.telEntry.insert(0, tel)
            self.emailEntry.insert(0, email)

    def clearEntry_student(self):
        self.idEntry.delete(0, "end")
        self.nameEntry.delete(0, "end")
        self.dateEntry.delete(0, "end")
        self.groupEntry.delete(0, "end")
        self.spEntry.delete(0, "end")
        self.telEntry.delete(0, "end")
        self.emailEntry.delete(0, "end")

    # Методы для таблицы student_additional_info
    def refreshTable_student_additional_info(self):
        self.tree_student_additional_info.delete(*self.tree_student_additional_info.get_children())
        rows = connection.get_rows(connection.select_student_additional_info())
        for row in rows:
            self.tree_student_additional_info.insert("", "end", values=list(row.values()))

    def updateRow_student_additional_info(self):
        connection.update_student(self.idEntry.get(), self.nameEntry.get(), self.dateEntry.get(),
                                  self.groupEntry.get(), self.spEntry.get(), self.telEntry.get(), self.emailEntry.get())
        self.refreshTable_student_additional_info()
        self.clearEntry_student_additional_info()

    def deleteRow_student_additional_info(self):
        connection.delete_from_student(self.idEntry.get())
        self.refreshTable_student_additional_info()
        self.clearEntry_student_additional_info()

    def insertRow_student_additional_info(self):
        connection.insert_into_student(self.nameEntry.get(), self.dateEntry.get(), self.groupEntry.get(),
                                       self.spEntry.get(), self.telEntry.get(), self.emailEntry.get())
        self.refreshTable_student_additional_info()
        self.clearEntry_student_additional_info()

    def get_selection_student_additional_info(self, event):
        self.clearEntry_student_additional_info()
        for selection in self.tree_student.selection():
            item = self.tree_student_additional_info.item(selection)
            id, name, date, group, sp, tel, email = item["values"][0:7]
            self.idEntry.insert(0, id)
            self.nameEntry.insert(0, name)
            self.dateEntry.insert(0, date)
            self.groupEntry.insert(0, group)
            self.spEntry.insert(0, sp)
            self.telEntry.insert(0, tel)
            self.emailEntry.insert(0, email)

    def clearEntry_student_additional_info(self):
        self.idEntry.delete(0, "end")
        self.nameEntry.delete(0, "end")
        self.dateEntry.delete(0, "end")
        self.groupEntry.delete(0, "end")
        self.spEntry.delete(0, "end")
        self.telEntry.delete(0, "end")
        self.emailEntry.delete(0, "end")

    # Методы для таблицы student_soft_skills
    # ...

    # Методы для таблицы student_education
    # ...

    # Методы для таблицы student_competencies
    # ...

    # Методы для таблицы decoding_competency_full
    # ...

    # Методы для таблицы specialty_code
    # ...

    # Методы для таблицы student_photo
    # ...


class AdminWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("1000x800")

        self.title("Jobkin")

        self.tab_view = TabView(master=self)
        self.tab_view.pack(expand=1, fill="both", padx=30, pady=30)
