# Ket noi voi database
import pyodbc
conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'SERVER=DESKTOP-50M8QJP\\SQLEXPRESS;'
                        'DATABASE=university;'
                        'Trusted_Connection=yes;')
cursor = conn.cursor()
#Func xoa sinh vien
def xoaSV(maSV):
    try:
        sql = "DELETE FROM thongtinSV WHERE maSV=?" # ? dac trung cho cho giu tham so
        cursor.execute(sql,(maSV,)) # (maSV,) tuple / [maSV] list truyen tham so
        conn.commit()
        print("Xoa thanh cong")
    except Exception as e:
        print("Error: ", e)
# Func in danh sach sinh vien
def danhsachSV():
    try:
        sql = "SELECT * FROM thongtinSV"
        cursor.execute(sql)
        conn.commit()
        rows = cursor.fetchall()
        for row in rows:
            print(f"Ma SV: {row.maSV}, Ho ten: {row.tenSV}, Ngay sinh: {row.ngaysinh}, Que quan: {row.quequan}")
    except Exception as e:
        print("Error: ",e) 
# Goi func xoaSV + danhsachSV
xoaSV(int(input("Nhap ma sinh vien can xoa: ")))
danhsachSV()
# Dong ket noi
cursor.close()
conn.close()
