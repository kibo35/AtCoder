S = list(input())
a = S.index('A')
z = len(S) - 1 - S[::-1].index('Z')
print(z - a + 1)