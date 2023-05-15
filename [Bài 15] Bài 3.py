lst = [int(i) for i in input().split()]

s = 0
for i in range(len(lst)):
    s += lst[i]
if s > 0:
    print("Chiếc giày còn thiếu ở bên trái, kích cỡ", abs(s))
else:
    print("Chiếc giày còn thiếu ở bên phải, kích cỡ", abs(s))
