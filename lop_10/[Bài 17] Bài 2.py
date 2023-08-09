nm = [int(i) for i in input().split()]
papb = [int(i) for i in input().split()]

t = 0
while (nm[1] + (papb[0] + papb[1]) * t) <= nm[0]:
    t += 1
print("Số ngày cần thiết là:", t)
