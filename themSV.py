# Tạo class thongtinSV và thuộc tính của nó
class thongtinSV:
    def __init__(self,maSV,tenSV,namsinh,quequan,nienkhoa,khoa):
        self.maSV = maSV
        self.tenSV = tenSV
        self.namsinh = namsinh
        self.quequan = quequan
        self.nienkhoa = nienkhoa
        self.khoa = khoa
# Method
    def themSV(self):
        # Kết nối với SQL
        import pyodbc
        conn = pyodbc.connect()

# Gán lớp và gọi function