create database university
use university
create table thongtinSV(
maSV int identity(100000,1) not null primary key,
tenSV varchar(100) not null,
ngaysinh date,
quequan varchar(100)
)