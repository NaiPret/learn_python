fileName = str(input("Nhập tên một tệp: "))

Length = len(fileName)
extensionName = fileName[-2:]
if extensionName == "py":
    print(fileName, "là tệp mã nguồn Python")
else:
    print(fileName, "không phải là tệp mã nguồn Python")
