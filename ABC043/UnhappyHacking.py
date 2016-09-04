s = raw_input()
words = []
for c in list(s):
    if c == 'B':
        if len(words) > 0:
            words.pop()
    else:
        words.append(c)
print ''.join(words)