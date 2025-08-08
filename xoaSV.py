# Kết nối với SQL
import pyodbc
conn = pyodbc.connect()
cursor = conn.cursor()
# Xây dựng hàm xóa sinh viên khỏi SQL
def xoaSV(maSV):
    sql = 