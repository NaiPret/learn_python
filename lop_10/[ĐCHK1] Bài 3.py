t_a = float(input("Thời gian chạy bộ là: "))
t_b = float(input("Thời gian đi bộ là: "))

v_b = 10.0
v_a = 20.0
v_c = 60.0
s = 300.0

s_a = v_a * t_a
s_b = v_b * t_b
s_c = s - s_a - s_b
t_c = s_c / v_c

print("Thời gian đi xe đò là:", t_c)
print("Quãng đường chạy bộ là:", s_a)
print("Quãng đường đi bộ là:", s_b)
print("Quãng đường đi xe đò là:", s_c)
