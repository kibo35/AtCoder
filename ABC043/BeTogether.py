import numpy as np
N = int(raw_input())
a = np.array(map(int, raw_input().split()))
cost = []
for y in xrange(a.min(), a.max() + 1):
    cost.append(np.sum((a - y) ** 2))
print min(cost)
