import numpy as np
s = np.array(list(raw_input()))
e = np.unique(s)
if len(e) % 2 == 1:
    print 'No'
elif len(e) == 2:
    if 'N' in e and 'S' in e:
        print 'Yes'
    elif 'W' in e and 'E' in e:
        print 'Yes'
    else:
        print 'No'
else:
    print 'Yes'