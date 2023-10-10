password = input("Nhập mật khẩu: ")

so_lan = 0
while (so_lan <= 3):
    if (password == "12345678"):
        print("Mật khẩu chính xác!")
        break
    if (so_lan == 3):
        print("Đã quá 3 lần sai mật khẩu! Vui lòng thử lại sau")
        break
    password = input("Mật khẩu sai! Vui lòng nhập lại lần " + str(so_lan + 1) + ": ")
    so_lan += 1
