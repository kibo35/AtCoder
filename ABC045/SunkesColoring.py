import numpy as np
H, W, N = map(int, raw_input().split())

board = np.zeros((H, W), dtype=np.uint8)
for _ in xrange(N):
    a, b = map(int, raw_input().split())
    board[a - 1, b - 1] = 1

hist = np.zeros(10, dtype=np.int)
for row in xrange(H - 2):
    for col in xrange(W - 2):
        patch = board[row:row + 3, col:col + 3]
        hist[patch.sum()] += 1

for i in xrange(10):
    print hist[i]