s = input('Dòng lệnh: ')
e = s.count('E')
w = s.count('W')
n = s.count('N')
s = s.count('S')
x = e - w
y = n - s

print('Toạ độ hiện tại của robot: (', x, ',',y, ')')
