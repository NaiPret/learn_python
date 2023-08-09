n = int(input("Nhập số nguyên n: "))

s = 0
i = 1
while (1/n >= 0.001):
    s += 1/i
    i += 1
print("Tổng S =", s)
