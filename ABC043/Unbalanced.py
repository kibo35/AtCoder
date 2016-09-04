s = list(raw_input())
unbalanced = False
for c in set(s):
    if s.count(c) >= len(s) / 2 + len(s) % 2:
        print s.index(c) + 1, len(s) - s[::-1].index(c)
        unbalanced = True
if not unbalanced:
    print -1, -1