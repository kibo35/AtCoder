import sys
s = list(raw_input())
if len(s) == 2:
    if s[0] == s[1]:
        print 1, 2
    else:
        print -1, -1
else:
    for n in [3]:
        for i in xrange(len(s) - n + 1):
            sub = s[i:i+n]
            for char in set(sub):
                if sub.count(char) >= n / 2 + n % 2:
                    print i + 1, i + n
                    sys.exit()
    print -1, -1
