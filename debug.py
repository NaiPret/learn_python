print("        ax² + bx + c = 0")
a = int(input(" + Nhập biến a: "))
b = int(input(" + Nhập biến b: "))
c = int(input(" + Nhập biến c: "))
print("\nKhi đó: %sx² +" % a, "%sx +" % b, "%s = 0" % c)
delta = b*b - 4*a*c
print(" + Delta = %s² -" % b, "4(%s *" % a, "%s) =" % c, delta)
print(-b + delta**(1/2))
print(-b - delta**(1/2))
x1 = (-b + delta**(1/2)) / (2.0*a)
x2 = (-b - delta**(1/2)) / (2.0*a)
print(" + Nghiệm x1 =", x1)
print(" + Nghiệm x2 =", x2)
print(-b + delta**(1/2))
print(-b - delta**(1/2))