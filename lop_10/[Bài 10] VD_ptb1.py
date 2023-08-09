def ptb1():
    a = int(input("a = "))
    b = int(input("b = "))
    if a != 0:
        print("Phương trình có nghiệm duy nhất:", -b / a)
    elif b == 0:
        print("Phương trình có vô số nghiệm.")
    else:
        print("Phương trình vô nghiệm.")

ptb1()
