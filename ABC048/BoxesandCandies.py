import numpy as np
N, x = map(int, input().split())
a = np.array((list(map(int, input().split()))), np.int32)
if x == 0:
    print(a.sum())
else:
    n = 0
    n += np.sum(a[a >= x] - x)
    a[a >= x] = x
    if len(a) % 2 == 0:
        b = a[::2]
    else:
        b = a[:-1:2]
    c = a[1::2]
    d = b + c
    n += np.sum(d[d >= x] - x)
    print(n)