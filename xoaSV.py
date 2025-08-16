# Ket noi voi database
import pyodbc
conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'SERVER=DESKTOP-50M8QJP\\SQLEXPRESS;'
                        'DATABASE=university;'
                        'Trusted_Connection=yes;')
cursor = conn.cursor()
# Ham xoa sinh vien
def xoaSV(maSV):
    try:
        sql = "DELETE FROM thongtinSV WHERE maSV = ?"
        cursor.excute(sql,maSV)
        conn.commit()
    except Exception as e: