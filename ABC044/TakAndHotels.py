N = int(raw_input())
K = int(raw_input())
X = int(raw_input())
Y = int(raw_input())
if N <= K:
    print X * N
else:
    print X * K + Y * (N - K)