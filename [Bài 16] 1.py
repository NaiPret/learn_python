p = int(input())
q = int(input())
lst = [int(i) for i in input().split()]
max = 0
for i in range(p, q+1): #q thành q+1
    if abs(lst[i]) > max:
        max = abs(lst[i])
print(max)
