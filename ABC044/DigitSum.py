import sys
import numpy as np
n = int(raw_input())
s = int(raw_input())

def f(b, n):
    if n < b:
        return n
    else:
        return f(b, int(np.floor(float(n)/b)))+(n%b)

if s == n:
    print n + 1
    sys.exit()

for b in xrange(2, n+1):
    if f(b, n) == s:
        print b
        sys.exit()
print -1