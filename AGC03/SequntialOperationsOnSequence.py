import numpy as np
N, Q = map(int, raw_input().split())
qs = []
for _ in xrange(Q):
    qs.append(int(raw_input()))
seq = np.arange(1, qs[0] + 1, dtype=np.int) % N
print seq