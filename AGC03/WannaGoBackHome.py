import numpy as np
s = np.array(list(raw_input()))
num_n = (s == 'N').sum()
num_e = (s == 'E').sum()
num_w = (s == 'W').sum()
num_s = (s == 'S').sum()
if num_n == num_s and num_e == num_w:
    print 'Yes'
else:
    print 'No'