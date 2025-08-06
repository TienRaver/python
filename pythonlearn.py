print("Chuong trình tính hằng đẳng thức")
# Nhập thư viện cần thiết
import math
# Nhập lựa chọn
print("Hãy chọn hằng đẳng thức:")
print("1. (a+b)^2")
print("2. (a-b)^2")
print("3. a^2-b^2")
# Thân chương trình
while True:
    luachon = int(input("Nhập lựa chọn của bạn: "))
    a = float(input("Nhập số a: "))
    b = float(input("Nhập số b: "))
    if luachon == 1:
        ketqua = math.pow(a,2)+2*a*b+math.pow(b,2)
        print("Kết quả là: ",round(ketqua,2))
    elif luachon == 2:
        ketqua = math.pow(a,2)-2*a*b+math.pow(b,2)
        print("Kết quả là: ",round(ketqua,2))
    elif luachon == 3:
        ketqua = (a+b)*(a-b)
        print("Kết quả là: ",round(ketqua,2))
    else:
        print("Nhập sai lựa chọn")
        break
    luachon1 = input("Bạn có muốn tiếp tục không (Y/N): ")
    if luachon1 == "Y" or "y":
        continue
    else:
        print("Chào tạm biệt!")
        break
#print("Chào tạm biệt!")