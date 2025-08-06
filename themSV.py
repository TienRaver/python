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
conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=DESKTOP-50M8QJP\\SQLEXPRESS;'
                        'Database=university;'
                        'Trusted_Connection=yes;')
cursor = conn.cursor()
# Xây dựng function thêm thông tin sinh viên
def themSV(self):
    try:
    except Exception as e:
        print("Lỗi kết nối cơ sở dữ liệu:", e)
# Gán lớp và gọi function