# https://practice.geeksforgeeks.org/problems/relative-sorting/0
# O(nlogn)when there is no elements in brr
import collections
for _ in range(int(input())):
    m,n=map(int,input().split())
    arr=list(map(int,input().split()))
    #not_included=set(arr)
    brr=list(map(int,input().split()))
    freq=collections.Counter(arr)
    res=[]
    for val in brr:
        res+=[val]*freq[val]
        #not_included.pop(val)
        del freq[val]
    for val in sorted(list(freq.keys())):
        res+=[val]*freq[val]
    print(*res)
        