#Bài 2:
A = int(input("Nhập chiều dài của đoạn đường (mét): "))
B = int(input("Nhập khoảng cách giữa các cây xanh (mét): "))
count = (A // B) + 1
print("Tổng số cây xanh cần phải trồng là", count)
#Bài 3 (dài):
v_b = 10.0
v_a = 20.0
v_c = 60.0
s = 300.0
t_a = float(input("Nhập thời gian chạy bộ (giờ): "))
t_b = float(input("Nhập thời gian đi bộ (giờ): "))
s_a = v_a * t_a
s_b = v_b * t_b
s_c = s - s_a - s_b
t_c = s_c / v_c
print("Thời gian đi xe đò là:", t_c, "(giờ)")
print("Quãng đường chạy bộ là:", s_a, "(km)")
print("Quãng đường đi bộ là:", s_b, "(km)")
print("Quãng đường đi xe đò là:", s_c, "(km)")
#Bài 3 (ngắn):
t_a = float(input("Nhập thời gian chạy bộ: "))
t_b = float(input("Nhập thời gian đi bộ: "))
s_a = 20.0 * t_a
s_b = 10.0 * t_b
s_c = 300.0 - s_a - s_b
print("Thời gian đi xe đò là:", s_c / 60.0)
print("Quãng đường chạy bộ là:", s_a)
print("Quãng đường đi bộ là:", s_b)
print("Quãng đường đi xe đò là:", s_c)
