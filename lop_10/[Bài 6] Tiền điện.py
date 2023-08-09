a = int(input("Nhập số điện tối đa ở mức 1: a = "))
b = int(input("Nhập số điện tối đa ở mức 2: b = "))
d1 = int(input("Nhập giá điện loại 1: d1 = "))
d2 = int(input("Nhập giá điện loại 2: d2 = "))
d3 = int(input("Nhập giá điện loại 3: d3 = "))
x = int(input("Nhập số điện người dùng tiêu thụ (kWh): x = "))

tien_dien = 0
if (x <= a):
    tien_dien = x * d1
if (a < x and x <= b):
    tien_dien = a * d1 + (x - a) * d2
if (x > b):
    tien_dien = a * d1 + (b - a) * d2 + (x - b) * d3

print("Số tiền điện phải trả là:", tien_dien)
