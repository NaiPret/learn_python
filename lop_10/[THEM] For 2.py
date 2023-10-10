# Viết chương trình tính tổng các số chẵn từ 0 đến 1000

s = 0
for i in range(0, 1001):
    if (i % 2 == 0):
        s += i
print("s =", s)
