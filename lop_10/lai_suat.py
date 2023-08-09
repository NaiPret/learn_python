k = float(input("Nhập lãi suất   (%): "))
A = float(input("Nhập tiền gửi (VNĐ): "))
B = float(input("Nhập mục tiêu (VNĐ): "))

thang = 0
tien_hien_co = A
tien_lai_hang_thang = A * (k / 100)
while (tien_hien_co < B):
    tien_hien_co += tien_lai_hang_thang
    thang += 1
print("Sau", thang, "tháng thì người đó rút được số tiền mục tiêu!")
