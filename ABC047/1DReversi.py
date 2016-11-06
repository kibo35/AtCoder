import numpy as np
S = input()
S1 = np.array(S.split("W"))
S2 = np.array(S.split("B"))
if len(S1) == 1 or len(S2) == 1:
    print(0)
else:
    num1 = len(S1[S1 != '']) * 2 - 1
    if S1[0] == '' and S1[-1] == '':
        num1 += 1
    if num1 < 0:
        num1 = 0
    num2 = len(S2[S2 != '']) * 2 - 1
    if S2[0] == '' and S2[-1] == '':
        num2 += 1
    if num2 < 0:
        num2 = 0
    if num2 < num1:
        print(num2)
    else:
        print(num1)