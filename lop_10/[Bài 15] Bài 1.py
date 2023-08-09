lst = [int(i) for i in input().split()]

for i in range(len(lst) - 1):
    if lst[i] > 0:
        lst[i] = 1
    else:
        lst[i] = -1
for i in lst[:]:
    print(i, end= " ")
