A, B, C = sorted(map(int, raw_input().split()))
print A * B * (C - (C // 2) * 2)