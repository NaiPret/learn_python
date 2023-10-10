def ptb1():
    a = int(input("Nhập biến a: "))
    b = int(input("Nhập biến b: "))
    x = -b / a
    print("Phương trình có nghiệm là: x =", x)

def ptb2():
    while (True):
        a = int(input("Nhập biến a: "))
        b = int(input("Nhập biến b: "))
        c = int(input("Nhập biến c: "))
        if (a == 0):
            print("Phương trình vô nghiệm")
            break
        d = (b**2) - (4*a*c)
        if (d < 0):
            print("Phương trình vô nghiệm")
            break
        if (d == 0):
            x = -b / (2*a)
            print("Phương trình có 1 nghiệm kép: x =", x)
            break
        if (d > 0):
            x1 = (-b + d**(1/2)) / (2.0 * a)
            x2 = (-b - d**(1/2)) / (2.0 * a)
            print("Phương trình có 2 nghiệm phân biệt: x1 =", x1, "x2 =", x2)
            break

while (True):
    print("**********************************")
    print("*         BẢNG CHỌN VIỆC         *")
    print("* 1. Giải phương trình bậc nhất  *")
    print("* 2. Giải phương trình bậc hai   *")
    print("* 3. Kết thúc chương trình       *")
    print("**********************************")
    chon = int(input("Hãy nhập lựa chọn của bạn: "))
    print()
    if (chon == 1):
        print("Giải phương trình bậc nhất: ax + b = 0")
        ptb1()
        break
    elif (chon == 2):
        print("Giải phương trình bậc hai: ax2 + bx + c = 0")
        ptb2()
        break
    else:
        print("Kết thúc chương trình")
        break
