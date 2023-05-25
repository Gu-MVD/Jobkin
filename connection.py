import pymysql
from config import *


class Connection:

    def open(self):
        try:
            global connection
            connection = pymysql.connect(host=host,
                                         port=3306,
                                         user=user,
                                         password=password,
                                         database=db_name,
                                         cursorclass=pymysql.cursors.DictCursor)
            print("Соединение установлено!")
        except Exception as ex:
            print("Error" + str(ex))

# Методы SELECT
    def select_student(self):
        try:
            with connection.cursor() as cursor:
                select_query = "select * from student"
                cursor.execute(select_query)
                rows = cursor.fetchall()
                return rows
        except Exception as ex:
            print("Error: " + str(ex))

    def get_columns(self):
        return list(self.select_student()[0].keys())

    def get_rows(self):
        return self.select_student()

    def select_student_soft_skills(self):
        try:
            with connection.cursor() as cursor:
                select_query = "select * from student_soft_skills"
                cursor.execute(select_query)
                rows = cursor.fetchall()
                return rows
        except Exception as ex:
            print("Error: " + str(ex))

    def select_student_education(self):
        try:
            with connection.cursor() as cursor:
                select_query = "select * from student_education"
                cursor.execute(select_query)
                rows = cursor.fetchall()
                return rows
        except Exception as ex:
            print("Error: " + str(ex))

    def select_student_competencies(self):
        try:
            with connection.cursor() as cursor:
                select_query = "select * from student_competencies"
                cursor.execute(select_query)
                rows = cursor.fetchall()
                return rows
        except Exception as ex:
            print("Error: " + str(ex))

    def select_student_additional_info(self):
        try:
            with connection.cursor() as cursor:
                select_query = "select * from student_additional_info"
                cursor.execute(select_query)
                rows = cursor.fetchall()
                return rows
        except Exception as ex:
            print("Error: " + str(ex))

    def select_specialty_code(self):
        try:
            with connection.cursor() as cursor:
                select_query = "select * from specialty_code"
                cursor.execute(select_query)
                rows = cursor.fetchall()
                return rows
        except Exception as ex:
            print("Error: " + str(ex))

    def select_decoding_competency_full(self):
        try:
            with connection.cursor() as cursor:
                select_query = "select * from decoding_competency_full"
                cursor.execute(select_query)
                rows = cursor.fetchall()
                return rows
        except Exception as ex:
            print("Error: " + str(ex))

    def select_student_photo(self):
        try:
            with connection.cursor() as cursor:
                select_query = "select * from student_photo"
                cursor.execute(select_query)
                rows = cursor.fetchall()
                return rows
        except Exception as ex:
            print("Error: " + str(ex))

# Методы INSERT
    def insert_into_student(self, STUDENTNAME: str, DATEOFBIRTH: str,
                            GROUPNUMBER: str,
                            SPECIALTYCODE: int,
                            TELNUMBER: str,
                            EMAILADDRESS: str):
        try:
            with connection.cursor() as cursor:
                insert_query = "insert into student (STUDENTNAME, DATEOFBIRTH," \
                               "GROUPNUMBER, SPECIALTYCODE, TELEPHONENUMBER," \
                               "EMAILADDRESS) " \
                               "values (%s, %s, %s, %s, %s, %s)"
                cursor.execute(insert_query,
                               (STUDENTNAME, DATEOFBIRTH, GROUPNUMBER, SPECIALTYCODE,
                                TELNUMBER, EMAILADDRESS))
            connection.commit()
        except Exception as ex:
            print("Error: " + str(ex))

    def insert_into_student_soft_skills(self, ID: int, FIRSTSOFSKILL: str, SECONDSOFSKILL: str, THIRDSOFSKILL: str,
                                        FOURTHOFSKILL: str, FIVETHSOFSKILL: str):
        try:
            with connection.cursor() as cursor:
                insert_query = "insert into student_soft_skills " \
                               "values (%s, %s, %s, %s, %s, %s)"
                cursor.execute(insert_query,
                               (ID, FIRSTSOFSKILL, SECONDSOFSKILL, THIRDSOFSKILL,
                                FOURTHOFSKILL, FIVETHSOFSKILL))
            connection.commit()
        except Exception as ex:
            print("Error: " + str(ex))

    def insert_into_student_education(self, ID: int, ESTABLISHMENT: str, FACULTY: str, FORMOFSTUDY: str,
                                        YEAROFENDING: str, CITY: str):
        try:
            with connection.cursor() as cursor:
                insert_query = "insert into student_education " \
                               "values (%s, %s, %s, %s, %s, %s)"
                cursor.execute(insert_query,
                               (ID, ESTABLISHMENT, FACULTY, FORMOFSTUDY,
                                YEAROFENDING, CITY))
            connection.commit()
        except Exception as ex:
            print("Error: " + str(ex))

    def insert_into_student_competencies(self, ID: int, COMPETENCE1: str):
        try:
            with connection.cursor() as cursor:
                insert_query = "insert into student_competencies " \
                               "values (%s, %s)"
                cursor.execute(insert_query,
                               (ID, COMPETENCE1))
            connection.commit()
        except Exception as ex:
            print("Error: " + str(ex))

    def insert_into_student_additional_info(self, ID: int, ADDITIONALINFO: str, FOREIGNLANGUAGE: str,
                                            DRIVERLICENSE: str, ADDITIONALCOMPETENCIES: str, SOCIALNETWORK: str):
        try:
            with connection.cursor() as cursor:
                insert_query = "insert into student_additional_info " \
                               "values (%s, %s, %s, %s, %s, %s)"
                cursor.execute(insert_query,
                               (ID, ADDITIONALINFO, FOREIGNLANGUAGE, DRIVERLICENSE,
                                ADDITIONALCOMPETENCIES, SOCIALNETWORK))
            connection.commit()
        except Exception as ex:
            print("Error: " + str(ex))

    def insert_into_specialty_code(self, SPECIALTYNAME: str):
        try:
            with connection.cursor() as cursor:
                insert_query = "insert into specialty_code (SPECIALTYNAME)" \
                               "values (%s)"
                cursor.execute(insert_query,
                               SPECIALTYNAME)
            connection.commit()
        except Exception as ex:
            print("Error: " + str(ex))

    def insert_into_decoding_competency_full(self, SPECIALTYCODE: int, COMPETENCE1: str, COMPETENCE2: str,
                                             COMPETENCE3: str, COMPETENCE4: str, COMPETENCE5: str):
        try:
            with connection.cursor() as cursor:
                insert_query = "insert into decoding_competency_full " \
                               "values (%s, %s, %s, %s, %s, %s)"
                cursor.execute(insert_query,
                               (SPECIALTYCODE, COMPETENCE1, COMPETENCE2, COMPETENCE3,
                                COMPETENCE4, COMPETENCE5))
            connection.commit()
        except Exception as ex:
            print("Error: " + str(ex))

    def insert_into_student_photo(self, ID: int, PHOTO: bytes):
        try:
            with connection.cursor() as cursor:
                insert_query = "insert into student_photo " \
                               "values (%s, %s)"
                cursor.execute(insert_query,
                               (ID, PHOTO))
            connection.commit()
        except Exception as ex:
            print("Error: " + str(ex))

# Методы DELETE
    def delete_from_student(self, ID: int):
        try:
            with connection.cursor() as cursor:
                delete_query = "delete from student where ID = %s" % ID
                cursor.execute(delete_query)
            connection.commit()
        except Exception as ex:
            print("Error: " + str(ex))

# Методы UPDATE
    def update_student(self, ID: int, STUDENTNAME: str,
                       DATEOFBIRTH: str,
                       GROUPNUMBER: str,
                       SPECIALTYCODE: int,
                       TELNUMBER: str,
                       EMAILADDRESS: str):
        try:
            with connection.cursor() as cursor:
                update_query = "update student set STUDENTNAME = %s, DATEOFBIRTH = %s, " \
                               "GROUPNUMBER = %s, SPECIALTYCODE = %s, TELEPHONENUMBER = %s, EMAILADDRESS = %s " \
                               "where ID = %s"
                cursor.execute(update_query,
                               (STUDENTNAME, DATEOFBIRTH, GROUPNUMBER, SPECIALTYCODE, TELNUMBER, EMAILADDRESS, ID))
            connection.commit()
        except Exception as ex:
            print("Error: " + str(ex))
