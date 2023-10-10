a = [int(i) for i in input().split()] # 5 3 2 2 1 2
b = a[:]               # b = a giống như gán 1 biến reference
n = len(a)
for i in range(1,n,2): #lẻ stt 1 3 5 7
    b[i] += 1          #đổi 0 thành 1 trong range
p = 0; q = 0
for i in range(n):
    if a[i] % 2 == 0:
        p += 1
    if b[i] & 1 == 0:
        q += 1
if p < q:
    print("Bé hơn")
elif p == q:
    print("Bằng nhau")
else:
    print("Lớn hơn")
