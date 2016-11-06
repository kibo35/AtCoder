W, H, N = map(int, input().split())
x0, y0 = 0, 0
x1, y1 = W, H
for _ in range(N):
    x, y, a = map(int, input().split())
    if a == 1 and x > x0:
        x0 = x
    elif a == 2 and x < x1:
        x1 = x
    elif a == 3 and y > y0:
        y0 = y
    elif a == 4 and y < y1:
        y1 = y
area = (x1 - x0) * (y1 - y0)
if area > 0:
    print(area)
else:
    print(0)