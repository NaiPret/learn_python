# Viết chương trình nhập vào một dãy số nguyên dương và đưa ra màn
# hình dãy đó có phải fibonaci hay không. Dãy fibonaci nếu a[0] = 0
# a[1] = 1,... a[i] = a[i-1] + a[i-2]
# Vd: 0,1,1,2,3,5,8,13,21

def is_fibonaci(lst):
    ans = True
    count = len(lst[:])
    for i in range(2, count):
        if lst[i] != lst[i-1] + lst[i-2]:
            ans = False
            break
    return ans

lst = [int(i) for i in input("Nhập dãy số cần phân tích: ").split()]

if is_fibonaci(lst) == True:
    print("Dãy số đã cho là dãy fibonaci")
else:
    print("Dãy số đã cho không phải là dãy fibonaci")
