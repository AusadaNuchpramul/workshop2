row = 1
while row <= 12:  # เเถว
    num = 2  # ( สูตรคูณเเม่ 2 )
    col = 2
    while col <= 12:
        print("%3dx%2d=%3d" % (num, row, num * row), end="")
        num += 1
        col += 1

    print("")
    row += 1

print("")
