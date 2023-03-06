def mtime(d, v1, v2):
    t = v1 + v2
    return d / t

d = float(input("d = "))
v1 = float(input("v1 = "))
v2 = float(input("v2 = "))
print("Hai xe gặp nhau sau", mtime(d, v1, v2), "giờ")
