Sa = list(raw_input())
Sb = list(raw_input())
Sc = list(raw_input())

def turn(card, Sa, Sb, Sc):
    if card == 'a':
        if len(Sa) == 0:
            print 'A'
        else:
            turn(Sa[0], Sa[1:], Sb, Sc)
    elif card == 'b':
        if len(Sb) == 0:
            print 'B'
        else:
            turn(Sb[0], Sa, Sb[1:], Sc)
    elif card == 'c':
        if len(Sc) == 0:
            print 'C'
        else:
            turn(Sc[0], Sa, Sb, Sc[1:])

turn('a', Sa, Sb, Sc)