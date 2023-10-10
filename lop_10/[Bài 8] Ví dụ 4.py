n = int(input("n = "))
sum = 0
for i in range(1, n):
    if (i % 3 == 0):
        sum += i
print("Tổng của dãy số tự nhiên nhỏ hơn", n, "và chia hết cho 3 là:", sum)
