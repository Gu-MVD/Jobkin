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

    def select_database(self):
        try:
            with connection.cursor() as cursor:
                select_query = "select * from student"
                cursor.execute(select_query)
                rows = cursor.fetchall()
                return rows
        except Exception as ex:
            print("Error: " + str(ex))

    def get_columns(self):
        return list(self.select_database()[0].keys())

    def get_rows(self):
        return self.select_database()

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

    def delete_from_student(self, ID: int):
        try:
            with connection.cursor() as cursor:
                delete_query = "delete from student where ID = %s" % ID
                cursor.execute(delete_query)
            connection.commit()
        except Exception as ex:
            print("Error: " + str(ex))

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
