diem = float(input("Nhập điểm trung bình môn học: "))

while (True):
    if (diem < 5):
        print("Xếp loại học sinh: Yếu kém")
        break
    elif (diem < 7):
        print("Xếp loại học sinh: Trung bình")
        break
    elif (diem < 8):
        print("Xếp loại học sinh: Khá")
        break
    elif (diem < 9):
        print("Xếp loại học sinh: Giỏi")
        break
    else:
        print("Xếp loại học sinh: Xuất sắc")
        break
