import numpy as np
N = int(raw_input())
A = []
for i in xrange(N):
    A.append(int(raw_input()))
A = np.array(A)
if np.argmin(A) % 2 == 0:
    print 0
else:
    print 1