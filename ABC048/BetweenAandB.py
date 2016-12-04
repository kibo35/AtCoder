import numpy as np
a, b, x = np.array(list(input().split()), dtype=np.uint64)
print(b // x - a // x + (b % x == 0))