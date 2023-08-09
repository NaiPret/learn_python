cha = int(input("Nhập tuổi cha: "))
con = int(input("Nhập tuổi con: "))

while (cha <= con or cha - con < 20 or cha - con > 45):
    cha = int(input("Nhập lại tuổi cha: "))
    con = int(input("Nhập lại tuổi con: "))

so_nam = 0
while (True):
    if (cha / (2 * con) == 1):
        print("Sau", so_nam, "năm. Khi cha", cha, "tuổi thì tuổi của cha gấp đôi tuổi con là", con)
        break
    if (cha > 120):
        print("Không có độ tuổi thỏa mãn đề bài!")
        break
    cha += 1
    con += 1
    so_nam += 1
