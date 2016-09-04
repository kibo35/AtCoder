import numpy as np
N = int(raw_input())
A = []
for i in xrange(N):
    A.append(int(raw_input()))
A = np.array(A)
num_pair = (A[A % 2 == 1] / 2).sum()
A[A % 2 == 1] = 1
num_pair += (A[A > 2] / 2).sum() - (A > 2).sum()
A[A > 2] = 2
for i in xrange(len(A) - 1):
    if A[i] == 2:
        num_pair += 1
        A[i] = 0
    elif A[i] == 1 and A[i + 1] >= 1:
        num_pair += 1
        A[i] = 0
        A[i + 1] -= 1
num_pair += A[-1] / 2
print num_pair
