import sys
import numpy as np
w = np.array(list(raw_input()))
for c in set(w):
    if (w == c).sum() % 2 == 1:
        print 'No'
        sys.exit()
print 'Yes'
