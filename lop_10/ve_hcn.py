def vehcn(chieu_dai, chieu_rong):
    sao = "*" * chieu_dai
    for i in range(chieu_rong):
        print(sao)

chieu_dai = int(input("Nhập chiều dài của hình chữ nhật: "))
chieu_rong = int(input("Nhập chiều rộng của hình chữ nhật: "))
vehcn(chieu_dai, chieu_rong)
