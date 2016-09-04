import numpy as np
input1 = raw_input()
input2 = raw_input()
N = int(input1)
list = input2.split()
a = np.zeros(len(list), np.uint8)
for i, element in enumerate(list):
    a[i] = int(element)

def play(turn, a, N):
    if N == 1 and a[0] == 1:
        if turn % 2 == 0:
            print 'Second'
        else:
            print 'First'
        return 0
                
    if (a - 1).sum() == 1:
        if turn % 2 == 0:
            print 'First'
        else:
            print 'Second'
        return 0

    if N == 2 and a.min() == 1:
        if turn % 2 == 0:
            print 'First'
        else:
            print 'Second'
        return 0

    if N == 2 and (a - 1).sum == 2:
        if turn % 2 == 0:
            print 'Second'
        else:
            print 'First'
        return 0

    if N == 1:
        a[0] -= 1
        play(turn + 1, a, 1)
    else:
        a[np.argmax(a)] = 0
        play(turn + 1, a[a > 0], N-1)

play(0, a, N)
