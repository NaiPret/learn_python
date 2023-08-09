from math import gcd

m = int(input("Nhập tử số m: "))
n = int(input("Nhập mẫu số n: "))

k = gcd(m, n)
print("Phân số", m, "/", n, "có dạng tối giản là", m/k, "/", n/k)
