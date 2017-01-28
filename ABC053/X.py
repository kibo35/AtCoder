x = int(input())
if x <= 6:
    print(1)
elif x <= 11:
    print(2)
else:
    y = x % 11
    if y == 0:
        print((x // 11) * 2)
    elif y <= 6:
        print((x // 11) * 2 + 1)
    else:
        print((x // 11) * 2 + 2)
