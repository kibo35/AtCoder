from itertools import combinations
import numpy as np
import math, sys
N, A = map(int, raw_input().split())
x = map(int, raw_input().split())
count = 0
for i in xrange(len(x)):
    for c in combinations(x, len(x) - i):
        if np.array(c).mean() == A:
            count += 1
print count