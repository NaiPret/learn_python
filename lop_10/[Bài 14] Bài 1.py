# Viết chương trình nhập một dãy số nguyên A và số nguyên k. Tìm và in ra
# màn hình phần tử có giá trị bằng k nếu có

lst = [int(i) for i in input("Nhập dãy số nguyên A: ").split()]
k = int(input("Nhập phần tử k cần tìm: "))

for i in range(len(lst)):
    if lst[i] == k:
        print("Phần tử", k, "xuất hiện tại vị trí", i + 1, "trong danh sách")
if lst.count(k) == 0:
    print("Phần tử", k, "không xuất hiện trong danh sách")
