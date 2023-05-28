import customtkinter as ctk
from tkinter import ttk
from connection import Connection
from CTkMessagebox import CTkMessagebox


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
        self.refreshButton_additional_info = ctk.CTkButton(self.additional_infoTab, text="refresh",
                                                           command=self.refreshTable_student_additional_info)
        self.updateButton_additional_info = ctk.CTkButton(self.additional_infoTab, text="update",
                                                          command=self.updateRow_student_additional_info)
        self.deleteButton_additional_info = ctk.CTkButton(self.additional_infoTab, text="delete",
                                                          command=self.deleteRow_student_additional_info)
        self.insertButton_additional_info = ctk.CTkButton(self.additional_infoTab, text="insert",
                                                          command=self.insertRow_student_additional_info)
        self.refreshButton_additional_info.pack(side="right", padx=(0, 44))
        self.updateButton_additional_info.pack(side="right", padx=20)
        self.deleteButton_additional_info.pack(side="right", padx=(20, 0))
        self.insertButton_additional_info.pack(side="right", padx=(20, 0))

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
        self.tree_student_soft_skills.bind("<<TreeviewSelect>>", self.get_selection_student_soft_skills)

        self.frame_student_soft_skills = ctk.CTkFrame(self.soft_skillsTab)
        self.id_soft_skillsEntry = ctk.CTkEntry(self.frame_student_soft_skills,
                                                placeholder_text="ID")
        self.first_skillEntry = ctk.CTkEntry(self.frame_student_soft_skills,
                                             placeholder_text="FIRSTSKILL")
        self.second_skillEntry = ctk.CTkEntry(self.frame_student_soft_skills,
                                              placeholder_text="SECONDSKILL")
        self.third_skillEntry = ctk.CTkEntry(self.frame_student_soft_skills,
                                             placeholder_text="THIRDSKILL")
        self.fourth_skillEntry = ctk.CTkEntry(self.frame_student_soft_skills,
                                              placeholder_text="FOURTHSKILL")
        self.fiveth_skillEntry = ctk.CTkEntry(self.frame_student_soft_skills,
                                              placeholder_text="FIVETHSKILL")
        self.frame_student_soft_skills.pack(padx=20, pady=10)
        self.id_soft_skillsEntry.pack(side="left")
        self.first_skillEntry.pack(side="left")
        self.second_skillEntry.pack(side="left")
        self.third_skillEntry.pack(side="left")
        self.fourth_skillEntry.pack(side="left")
        self.fiveth_skillEntry.pack(side="left")

        # Кнопки для действий с таблицей
        self.refreshButton_soft_skills = ctk.CTkButton(self.soft_skillsTab, text="refresh",
                                                       command=self.refreshTable_student_soft_skills)
        self.updateButton_soft_skills = ctk.CTkButton(self.soft_skillsTab, text="update",
                                                      command=self.updateRow_student_soft_skills)
        self.deleteButton_soft_skills = ctk.CTkButton(self.soft_skillsTab, text="delete",
                                                      command=self.deleteRow_student_soft_skills)
        self.insertButton_soft_skills = ctk.CTkButton(self.soft_skillsTab, text="insert",
                                                      command=self.insertRow_student_soft_skills)
        self.refreshButton_soft_skills.pack(side="right", padx=(0, 44))
        self.updateButton_soft_skills.pack(side="right", padx=20)
        self.deleteButton_soft_skills.pack(side="right", padx=(20, 0))
        self.insertButton_soft_skills.pack(side="right", padx=(20, 0))

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
        self.tree_student_education.bind("<<TreeviewSelect>>", self.get_selection_student_education)

        self.frame_student_educational = ctk.CTkFrame(self.educationTab)
        self.id_educationalEntry = ctk.CTkEntry(self.frame_student_educational,
                                                placeholder_text="ID")
        self.establishmentEntry = ctk.CTkEntry(self.frame_student_educational,
                                               placeholder_text="ESTABLISHMENT")
        self.facultyEntry = ctk.CTkEntry(self.frame_student_educational,
                                         placeholder_text="FACULTY")
        self.form_of_studyEntry = ctk.CTkEntry(self.frame_student_educational,
                                               placeholder_text="FORMOFSTUDY")
        self.year_of_endingEntry = ctk.CTkEntry(self.frame_student_educational,
                                                placeholder_text="YEAROFENDING")
        self.cityEntry = ctk.CTkEntry(self.frame_student_educational,
                                      placeholder_text="CITY")
        self.frame_student_educational.pack(padx=20, pady=10)
        self.id_educationalEntry.pack(side="left")
        self.establishmentEntry.pack(side="left")
        self.facultyEntry.pack(side="left")
        self.form_of_studyEntry.pack(side="left")
        self.year_of_endingEntry.pack(side="left")
        self.cityEntry.pack(side="left")

        # Кнопки для действий с таблицей
        self.refreshButton_educational = ctk.CTkButton(self.educationTab, text="refresh",
                                                       command=self.refreshTable_student_education)
        self.updateButton_educational = ctk.CTkButton(self.educationTab, text="update",
                                                      command=self.updateRow_student_education)
        self.deleteButton_educational = ctk.CTkButton(self.educationTab, text="delete",
                                                      command=self.deleteRow_student_education)
        self.insertButton_educational = ctk.CTkButton(self.educationTab, text="insert",
                                                      command=self.insertRow_student_education)
        self.refreshButton_educational.pack(side="right", padx=(0, 44))
        self.updateButton_educational.pack(side="right", padx=20)
        self.deleteButton_educational.pack(side="right", padx=(20, 0))
        self.insertButton_educational.pack(side="right", padx=(20, 0))

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
        self.tree_specialty_code.bind("<<TreeviewSelect>>", self.get_selection_specialty_code)

        self.frame_specialty_code = ctk.CTkFrame(self.specialtyTab)
        self.specialty_codeEntry = ctk.CTkEntry(self.frame_specialty_code,
                                                placeholder_text="SPECIALTYCODE")
        self.specialty_nameEntry = ctk.CTkEntry(self.frame_specialty_code,
                                                placeholder_text="SPECIALTYNAME")
        self.frame_specialty_code.pack(padx=20, pady=10)
        self.specialty_codeEntry.pack(side="left")
        self.specialty_nameEntry.pack(side="left")

        # Кнопки для действий с таблицей
        self.refreshButton_specialty_code = ctk.CTkButton(self.specialtyTab, text="refresh",
                                                          command=self.refreshTable_specialty_code)
        self.updateButton_specialty_code = ctk.CTkButton(self.specialtyTab, text="update",
                                                         command=self.updateRow_specialty_code)
        self.deleteButton_specialty_code = ctk.CTkButton(self.specialtyTab, text="delete",
                                                         command=self.deleteRow_specialty_code)
        self.insertButton_specialty_code = ctk.CTkButton(self.specialtyTab, text="insert",
                                                         command=self.insertRow_specialty_code)
        self.refreshButton_specialty_code.pack(side="right", padx=(0, 44))
        self.updateButton_specialty_code.pack(side="right", padx=20)
        self.deleteButton_specialty_code.pack(side="right", padx=(20, 0))
        self.insertButton_specialty_code.pack(side="right", padx=(20, 0))

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
        self.tree_student_photo.bind("<<TreeviewSelect>>", self.get_selection_student_photo)

        self.frame_student_photo = ctk.CTkFrame(self.photoTab)
        self.id_photoEntry = ctk.CTkEntry(self.frame_student_photo,
                                          placeholder_text="ID")
        self.photoEntry = ctk.CTkEntry(self.frame_student_photo,
                                       placeholder_text="PHOTO")
        self.frame_student_photo.pack(padx=20, pady=10)
        self.id_photoEntry.pack(side="left")
        self.photoEntry.pack(side="left")

        # Кнопки для действий с таблицей
        self.refreshButton_photo = ctk.CTkButton(self.photoTab, text="refresh",
                                                 command=self.refreshTable_student_photo)
        self.updateButton_photo = ctk.CTkButton(self.photoTab, text="update",
                                                command=self.updateRow_student_photo)
        self.deleteButton_photo = ctk.CTkButton(self.photoTab, text="delete",
                                                command=self.deleteRow_student_photo)
        self.insertButton_photo = ctk.CTkButton(self.photoTab, text="insert",
                                                command=self.insertRow_student_photo)
        self.refreshButton_photo.pack(side="right", padx=(0, 44))
        self.updateButton_photo.pack(side="right", padx=20)
        self.deleteButton_photo.pack(side="right", padx=(20, 0))
        self.insertButton_photo.pack(side="right", padx=(20, 0))

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
        connection.update_student_additioanl_info(self.add_info_add_infoEntry.get(),
                                                  self.foreign_language_add_infoEntry.get(),
                                                  self.driver_license_add_infoEntry.get(),
                                                  self.add_competencies_add_infoEntry.get(),
                                                  self.social_network_add_infoEntry.get(), self.id_add_infoEntry.get())
        self.refreshTable_student_additional_info()
        self.clearEntry_student_additional_info()

    def deleteRow_student_additional_info(self):
        connection.delete_from_student_additional_info(self.id_add_infoEntry.get())
        self.refreshTable_student_additional_info()
        self.clearEntry_student_additional_info()

    def insertRow_student_additional_info(self):
        connection.insert_into_student_additional_info(self.id_add_infoEntry.get(), self.add_info_add_infoEntry.get(),
                                                       self.foreign_language_add_infoEntry.get(),
                                                       self.driver_license_add_infoEntry.get(),
                                                       self.add_competencies_add_infoEntry.get(),
                                                       self.social_network_add_infoEntry.get())
        self.refreshTable_student_additional_info()
        self.clearEntry_student_additional_info()

    def get_selection_student_additional_info(self, event):
        self.clearEntry_student_additional_info()
        for selection in self.tree_student_additional_info.selection():
            item = self.tree_student_additional_info.item(selection)
            add_info, foreign_language, driver_license, add_competencies, social_network, id = item["values"][0:6]
            self.add_info_add_infoEntry.insert(0, add_info)
            self.foreign_language_add_infoEntry.insert(0, foreign_language)
            self.driver_license_add_infoEntry.insert(0, driver_license)
            self.add_competencies_add_infoEntry.insert(0, add_competencies)
            self.social_network_add_infoEntry.insert(0, social_network)
            self.id_add_infoEntry.insert(0, id)

    def clearEntry_student_additional_info(self):
        self.add_info_add_infoEntry.delete(0, "end")
        self.foreign_language_add_infoEntry.delete(0, "end")
        self.driver_license_add_infoEntry.delete(0, "end")
        self.add_competencies_add_infoEntry.delete(0, "end")
        self.social_network_add_infoEntry.delete(0, "end")
        self.id_add_infoEntry.delete(0, "end")

    # Методы для таблицы student_soft_skills
    def refreshTable_student_soft_skills(self):
        self.tree_student_soft_skills.delete(*self.tree_student_soft_skills.get_children())
        rows = connection.get_rows(connection.select_student_soft_skills())
        for row in rows:
            self.tree_student_soft_skills.insert("", "end", values=list(row.values()))

    def updateRow_student_soft_skills(self):
        connection.update_student_soft_skills(self.id_soft_skillsEntry.get(),
                                              self.first_skillEntry.get(),
                                              self.second_skillEntry.get(),
                                              self.third_skillEntry.get(),
                                              self.fourth_skillEntry.get(), self.fiveth_skillEntry.get())
        self.refreshTable_student_soft_skills()
        self.clearEntry_student_soft_skills()

    def deleteRow_student_soft_skills(self):
        connection.delete_from_student_soft_skills(self.id_soft_skillsEntry.get())
        self.refreshTable_student_soft_skills()
        self.clearEntry_student_soft_skills()

    def insertRow_student_soft_skills(self):
        connection.insert_into_student_soft_skills(self.id_soft_skillsEntry.get(), self.first_skillEntry.get(),
                                                   self.second_skillEntry.get(), self.third_skillEntry.get(),
                                                   self.fourth_skillEntry.get(), self.fiveth_skillEntry.get())
        self.refreshTable_student_soft_skills()
        self.clearEntry_student_soft_skills()

    def get_selection_student_soft_skills(self, event):
        self.clearEntry_student_soft_skills()
        for selection in self.tree_student_soft_skills.selection():
            item = self.tree_student_soft_skills.item(selection)
            id, first, second, third, fourth, fiveth = item["values"][0:6]
            self.id_soft_skillsEntry.insert(0, id)
            self.first_skillEntry.insert(0, first)
            self.second_skillEntry.insert(0, second)
            self.third_skillEntry.insert(0, third)
            self.fourth_skillEntry.insert(0, fourth)
            self.fiveth_skillEntry.insert(0, fiveth)

    def clearEntry_student_soft_skills(self):
        self.id_soft_skillsEntry.delete(0, "end")
        self.first_skillEntry.delete(0, "end")
        self.second_skillEntry.delete(0, "end")
        self.third_skillEntry.delete(0, "end")
        self.fourth_skillEntry.delete(0, "end")
        self.fiveth_skillEntry.delete(0, "end")

    # Методы для таблицы student_education
    def refreshTable_student_education(self):
        self.tree_student_education.delete(*self.tree_student_education.get_children())
        rows = connection.get_rows(connection.select_student_education())
        for row in rows:
            self.tree_student_education.insert("", "end", values=list(row.values()))

    def updateRow_student_education(self):
        connection.update_student_education(self.id_educationalEntry.get(), self.establishmentEntry.get(),
                                            self.facultyEntry.get(), self.form_of_studyEntry.get(),
                                            self.year_of_endingEntry.get(), self.cityEntry.get())
        self.refreshTable_student_education()
        self.clearEntry_student_education()

    def deleteRow_student_education(self):
        connection.delete_from_student_education(self.id_educationalEntry.get())
        self.refreshTable_student_education()
        self.clearEntry_student_education()

    def insertRow_student_education(self):
        connection.insert_into_student_education(self.id_educationalEntry.get(), self.establishmentEntry.get(),
                                                 self.facultyEntry.get(), self.form_of_studyEntry.get(),
                                                 self.year_of_endingEntry.get(), self.cityEntry.get())
        self.refreshTable_student_education()
        self.clearEntry_student_education()

    def get_selection_student_education(self, event):
        self.clearEntry_student_education()
        for selection in self.tree_student_education.selection():
            item = self.tree_student_education.item(selection)
            id, establishment, faculty, form_of_study, year_of_ending, city = item["values"][0:6]
            self.id_educationalEntry.insert(0, id)
            self.establishmentEntry.insert(0, establishment)
            self.facultyEntry.insert(0, faculty)
            self.form_of_studyEntry.insert(0, form_of_study)
            self.year_of_endingEntry.insert(0, year_of_ending)
            self.cityEntry.insert(0, city)

    def clearEntry_student_education(self):
        self.id_educationalEntry.delete(0, "end")
        self.establishmentEntry.delete(0, "end")
        self.facultyEntry.delete(0, "end")
        self.form_of_studyEntry.delete(0, "end")
        self.year_of_endingEntry.delete(0, "end")
        self.cityEntry.delete(0, "end")

    # Методы для таблицы student_competencies
    # ...

    # Методы для таблицы decoding_competency_full
    # ...

    # Методы для таблицы specialty_code
    def refreshTable_specialty_code(self):
        self.tree_specialty_code.delete(*self.tree_specialty_code.get_children())
        rows = connection.get_rows(connection.select_specialty_code())
        for row in rows:
            self.tree_specialty_code.insert("", "end", values=list(row.values()))

    def updateRow_specialty_code(self):
        connection.update_specialty_code(self.specialty_codeEntry.get(), self.specialty_nameEntry.get())
        self.refreshTable_specialty_code()
        self.clearEntry_specialty_code()

    def deleteRow_specialty_code(self):
        connection.delete_from_specialty_code(self.specialty_codeEntry.get())
        self.refreshTable_specialty_code()
        self.clearEntry_specialty_code()

    def insertRow_specialty_code(self):
        connection.insert_into_specialty_code(self.specialty_nameEntry.get())
        self.refreshTable_specialty_code()
        self.clearEntry_specialty_code()

    def get_selection_specialty_code(self, event):
        self.clearEntry_specialty_code()
        for selection in self.tree_specialty_code.selection():
            item = self.tree_specialty_code.item(selection)
            specialty_code, specialty_name = item["values"][0:2]
            self.specialty_codeEntry.insert(0, specialty_code)
            self.specialty_nameEntry.insert(0, specialty_name)

    def clearEntry_specialty_code(self):
        self.specialty_codeEntry.delete(0, "end")
        self.specialty_nameEntry.delete(0, "end")

    # Методы для таблицы student_photo
    def refreshTable_student_photo(self):
        self.tree_student_photo.delete(*self.tree_student_photo.get_children())
        rows = connection.get_rows(connection.select_student_photo())
        for row in rows:
            self.tree_student_photo.insert("", "end", values=list(row.values()))

    def updateRow_student_photo(self):
        connection.update_student_photo(self.id_photoEntry.get(), self.photoEntry.get())
        self.refreshTable_student_photo()
        self.clearEntry_student_photo()

    def deleteRow_student_photo(self):
        connection.delete_from_student_photo(self.id_photoEntry.get())
        self.refreshTable_student_photo()
        self.clearEntry_student_photo()

    def insertRow_student_photo(self):
        connection.insert_into_student_photo(self.id_photoEntry.get(), self.photoEntry.get())
        self.refreshTable_student_photo()
        self.clearEntry_student_photo()

    def get_selection_student_photo(self, event):
        self.clearEntry_student_photo()
        for selection in self.tree_student_photo.selection():
            item = self.tree_student_photo.item(selection)
            id_photo, photo = item["values"][0:2]
            self.id_photoEntry.insert(0, id_photo)
            self.photoEntry.insert(0, photo)

    def clearEntry_student_photo(self):
        self.id_photoEntry.delete(0, "end")
        self.photoEntry.delete(0, "end")


class AdminWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.info_window = None
        self.geometry("1000x800+460+40")

        self.title("Jobkin")

        # Предпросмотр резюме
        self.frame_search = ctk.CTkFrame(self)
        self.frame_search.pack(padx=30, pady=20)
        self.searchLabel = ctk.CTkLabel(self.frame_search, text="Поиск резюме")
        self.searchLabel.pack()
        self.search_idEntry = ctk.CTkEntry(self.frame_search, placeholder_text="ID", width=50)
        self.searchButton = ctk.CTkButton(self.frame_search, text="Search", command=self.search_resume)
        self.search_idEntry.pack(side="left", pady=(0, 10), padx=10)
        self.searchButton.pack(side="left", pady=(0, 10), padx=(0, 10))
        self.tab_view = TabView(master=self)
        self.tab_view.pack(expand=1, fill="both", padx=30, pady=(0, 10))

    def search_resume(self):
        try:
            resume = connection.show_resume(self.search_idEntry.get())
            self.search_idEntry.delete(0, "end")
            message = f"ФИО: {resume[0]['STUDENTNAME']}\nДата рождения: {resume[0]['DATEOFBIRTH']}\nНомер группы: {resume[0]['GROUPNUMBER']}\n" \
                      f"Специальность: {resume[0]['SPECIALTYNAME']}\nНомер телефона: {resume[0]['TELEPHONENUMBER']}\n" \
                      f"Иностранные языки: {resume[0]['FOREIGNLANGUAGE']}"
            self.info_window = CTkMessagebox(title="Info", message=message, option_1="Cancel")
        except Exception:
            self.info_window = CTkMessagebox(title="Info", message="Информация о студенте неполная", option_1="Cancel")

        response = self.info_window.get()
        if response == "Cancel":
            self.info_window.destroy()
