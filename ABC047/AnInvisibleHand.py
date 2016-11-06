import numpy as np
N, T = map(int, input().split())
A = np.array(list(map(int, input().split())))
B = A < np.roll(A, 1)
C = A < np.roll(A, -1)
print(np.sum((B * C)[:-1]))
