# Khai bao class
class sinhvien:
    def __init__(self,tenSV,ngaysinh,quequan):
        self.tenSV = tenSV
        self.ngaysinh = ngaysinh
        self.quequan = quequan
# Ket noi voi database
import pyodbc
conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'SERVER=DESKTOP-50M8QJP\\SQLEXPRESS;'
                        'DATABASE=university;'
                        'Trusted_Connection=yes;')
cursor = conn.cursor()
# Tao func themSV
def themSV(sinhvien):
    try:
        sql = "insert into thongtinSV(tenSV,ngaysinh,quequan) values(?,?,?)"
        cursor.execute(sql,sinhvien.tenSV,sinhvien.ngaysinh,sinhvien.quequan)
        conn.commit() # Luu thay doi vao database
        # In ra danh sach sinh vien
        print("Them sinh vien thanh cong")
    except Exception as e:
        print("Error: ", e)
# Tao function in danh sach sinh vien
def danhsachSV():
    try:
        sql = "SELECT * FROM thongtinSV"
        cursor.execute(sql)
        rows = cursor.fetchall()
        print("Danh sach sinh vien:")
        for row in rows:
            print(f"Ma SV: {row.maSV}, Ten SV: {row.tenSV}, Ngay sinh: {row.ngaysinh}, Que quan: {row.quequan}")
    except Exception as e:
        print("Error: ", e)
# Tao doi tuong sinh vien
from datetime import datetime # Nhap thu vien thoi gian
sinhvien1 = sinhvien(input("Nhap ten sinh vien: "),
                     #Chuyen doi dinh dang ngay thang
                     datetime.strptime(input("Nhap ngay sinh (dd/mm/yyyy): "),"%d/%m/%Y").date(),
                    input("Nhap que quan: "))
# Goi func themSV va danhsachSV
themSV(sinhvien1)
danhsachSV()
# Dong ket noi
cursor.close()
conn.close()
