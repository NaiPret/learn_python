#Viết chương trình nhập số học sinh  trong 1 tổ, nhập cân nặng và chiều cao cho
#từng bạn. Tính và đưa ra chỉ số BMI cho từng bạn

def BMI(chieu_cao, can_nang, i):
    BMI = can_nang / (chieu_cao/100) ** 2
    print("Chỉ số BMI của bạn số", i+1, "là: ", round(BMI, 2))

so_hoc_sinh = int(input("Nhập số học sinh trong tổ: "))
for i in range(so_hoc_sinh):
    print()
    chieu_cao = float(input("Nhập chiều cao của bạn số " + str(i+1) + ": "))
    can_nang= float(input("Nhập cân nặng của bạn số " + str(i+1) + ": "))
    BMI(chieu_cao, can_nang, i)
