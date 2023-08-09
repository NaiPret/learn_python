# Bài 3

n = int(input("Nhập số nguyên n = "))
s = 0
for i in range(1, n+1):
    if i % 2 == 0:
        s += i
print("Tổng các số chẵn là:", s)