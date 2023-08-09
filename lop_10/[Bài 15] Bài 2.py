lst = [int(i) for i in input().split()]

count = 0
for i in range(1, len(lst) - 1):
    if lst[i-1] < lst[i] and lst[i] > lst[i+1]:
        count += 1
print(count)
