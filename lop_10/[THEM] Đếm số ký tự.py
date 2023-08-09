n = int(input())

c = 1
while (n // 10 != 0):
    n //= 10
    c += 1
print(c)
