# Bài 4

a = [int(i) for i in input("Nhập danh sách: ").split()]
s = 0
for i in a[:]:
    if i < 0:
        s += i
print("Tổng các phần tử âm =", s)