ho_va_ten = str(input("Nhập họ và tên cần lọc: "))

tong_so_dau_cach = ho_va_ten.count(" ")
print()
while (True):
    if (tong_so_dau_cach < 1):
        print("Tên là:", ho_va_ten)
        break
    if (tong_so_dau_cach < 2):
        dau_cach_p = ho_va_ten.find(" ")
        print("Họ là:", ho_va_ten[:dau_cach_p])
        print("Tên là:", ho_va_ten[dau_cach_p + 1:])
        break
    dau_cach_s = ho_va_ten[:].find(" ")
    for i in range(len(ho_va_ten)):
        if ho_va_ten[i] == " ":
            dau_cach_e = i
    print("Họ là:", ho_va_ten[:dau_cach_s])
    print("Tên đệm là:", ho_va_ten[dau_cach_s + 1:dau_cach_e])
    print("Tên là:", ho_va_ten[dau_cach_e + 1:])
    break
