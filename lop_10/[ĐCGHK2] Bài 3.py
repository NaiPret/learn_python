m = int(input("Nhập số nguyên m: "))
n = int(input("Nhập số nguyên n: "))

tong = 0
for i in range(m, n + 1):
    tong += i
print("Tổng các số nguyên từ", m, "đến", n, "là:", tong)
