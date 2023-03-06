diem = float(input("Nhập điểm trung bình môn toán: "))

if (diem < 5):
    print("Học sinh yếu, kém")
if (diem < 6.5 and diem >= 5):
    print("Học sinh trung bình")
if (diem < 8 and diem >= 6.5):
    print("Học sinh khá")
if (diem >= 8):
    print("Học sinh giỏi")
