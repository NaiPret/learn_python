import time
tb = time.time()
n = 0
s = 0
x = int(input())
while x > 0:
    n += 1
    s += x
    x = int(input())
if n > 0:
    print("Trung bình cộng:", s / n)
print()
print("Time:", time.time() - tb, "sec")
