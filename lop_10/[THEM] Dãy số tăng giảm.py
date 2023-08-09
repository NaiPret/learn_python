# Đưa thông báo ra màn hình dãy số là dãy tăng / giảm / không phải
# là dãy tăng giảm

lst = [int(i) for i in input("Nhập dãy số cần phân tích: ").split()]

lst_count = len(lst)
lst_temp = lst.copy()

lst_temp.sort()
if lst == lst_temp:
    print("Dãy số trên là dãy tăng dần")
lst_temp.sort(reverse=True)
if lst == lst_temp:
    print("Dãy số trên là dãy giảm dần")
else:
    print("Dãy số trên không phải là dãy tăng giảm")
