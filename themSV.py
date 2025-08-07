# Tạo class thongtinSV và thuộc tính của nó
class sinhvien:
    def __init__(self,ID,tenSV,ngaysinh,gioitinh,quequan,nienkhoa,khoa):
        self.ID = ID
        self.tenSV = tenSV
        self.ngaysinh = ngaysinh
        self.gioitinh = gioitinh
        self.quequan = quequan
        self.nienkhoa = nienkhoa
        self.khoa = khoa
# Kết nối với SQL
import pyodbc
from datetime import datetime
conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=DESKTOP-50M8QJP\\SQLEXPRESS;'
                        'Database=university;'
                        'Trusted_Connection=yes;')
cursor = conn.cursor()
# Xây dựng function thêm thông tin sinh viên
def themSV(sinhvien):
    try:
        sql = "insert into student(ID,tenSV,ngaysinh,gioitinh,quequan,nienkhoa,khoa)" \
        "value (?,?,?,?,?,?,?)"
        cursor.excute(sql,sinhvien.ID,sinhvien.tenSV,sinhvien.ngaysinh,sinhvien.gioitinh,
                      sinhvien.quequan,sinhvien.nienkhoa,sinhvien.khoa)
        conn.commit()
        print("Thêm thành công")
        for i in cursor.fetchall(): # In tất cả sinh viên trong danh sách ra
            print(i)
    except Exception as e:
        print("Error: ", e)
# Gán lớp sinhvien
sinhvien1 = sinhvien(
    int(input("ID: ")),
    input("Tên sinh viên: "),
    datetime.strptime(input("Ngày sinh: "),"%d/%m/%Y"),
    input("Giới tính Nam/Nữ/Không xác định: "),
    input("Quê quán: "),
    input("Niên khóa: "),
    input("Khoa: ")
)
# Gọi function thêm sinh viên và đóng kết nối SQL
themSV(sinhvien1)
cursor.close()
conn.close()