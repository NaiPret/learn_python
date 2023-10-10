def BMI(chieu_cao, can_nang, i):
    BMI = can_nang / (chieu_cao/100) ** 2
    print("Chỉ số BMI của bạn số", i, "là:", round(BMI, 2))

so_hoc_sinh = int(input("Nhập số học sinh trong tổ: "))
for i in range(1, so_hoc_sinh + 1):
    print()
    chieu_cao = float(input("Nhập chiều cao của bạn số " + str(i) + " là: "))
    can_nang = float(input("Nhập cân nặng của bạn số " + str(i) + " là: "))
    BMI(chieu_cao, can_nang, i)
