input = raw_input()
a, b = input.split()
a = int(a)
b = int(b)
if a > 0 and b > 0:
    print 'Positive'
elif a < 0 and b < 0:
    if (b - a) % 2 == 0:
        print 'Negative'
    else:
        print 'Positive'
else:
    print 'Zero'
