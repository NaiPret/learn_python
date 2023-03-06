a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

max = a
if (max < b):
    max = b
if (max < c):
    max = c
print("Số lớn nhất là:", max)
