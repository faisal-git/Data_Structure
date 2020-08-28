# https://practice.geeksforgeeks.org/problems/check-frequencies/0

import collections
for _ in range(int(input())):
    s=input()
    # to calculate the freq.
    freq=collections.Counter(s)
    # how many uniqu freq and what r there counts
    cnt_freq=collections.Counter(freq.values())

    # if all characters have same freq 
    if len(cnt_freq)==1:
        print(1)
    # if there are more 2 unique freq
    elif len(cnt_freq)>2:
        print(0)
    else:
        # if out of two freq one has to have count 1
        if 1 in cnt_freq.values():
            f=list(cnt_freq.keys())
            # the differnce between freq should be one
            if abs(f[0]-f[1])==1:
                print(1)
            else:print(0)
        else:
            print(0)