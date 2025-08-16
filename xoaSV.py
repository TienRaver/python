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
        sql = "DELETE FROM thongtinSV WHERE maSV=?" # ? dac trung cho cho giu tham so
        cursor.execute(sql,(maSV,)) # (maSV,) tuple / [maSV] list truyen tham so
        conn.commit()
        print("Xoa thanh cong")
    except Exception as e:
        print("Error:", e)
# Goi ham xoaSV
xoaSV(int(input("Nhap ma sinh vien can xoa: ")))
# Dong ket noi
cursor.close()
conn.close()
