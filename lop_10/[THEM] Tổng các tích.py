m = int(input("Nhập M = "))

s = 0
for i in range(1, m + 1):
    for j in range(1, 10 + 1):
        s += i * j
print("Tổng S =", s)
