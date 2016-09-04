import numpy as np
N, x = map(int, raw_input().split())
a = np.array(map(int, raw_input().split()))

if max(a) <= x:
    print sum(a)
else:
    flg = a <= x
    t = sum(a[flg])
    flg = np.roll(flg, 1)
    t += x
    
    while (flg == False).sum() > 0:
        ndx = np.where(flg == False)[0]
        i = np.argmin(a[ndx])
        if a[i] <= x:
            t += a[i]
            flg[i] = True
        else:
            t += x
            flg = np.roll(flg, 1)

    print t
