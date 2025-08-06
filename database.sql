create database university
USE university
CREATE TABLE student (
    ID INT IDENTITY(1000000,1) PRIMARY KEY NOT NULL,
    tenSV VARCHAR(100) NOT NULL,
    ngaysinh DATE NOT NULL,
    gioitinh VARCHAR(20) NOT NULL,
    quequan VARCHAR(100) NOT NULL,
    nienkhoa VARCHAR(20) NOT NULL,
    khoa VARCHAR(100) NOT NULL,
)