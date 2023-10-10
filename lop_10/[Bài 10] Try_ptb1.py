def ptb1(a, b):
    if a != 0:
        print("Phương trình có nghiệm duy nhất:", -b / a)
    elif b == 0:
        print("Phương trình có vô số nghiệm.")
    else:
        print("Phương trình vô nghiệm.")

ptb1(5, 4)
ptb1(0, 0)
ptb1(0, 4)
