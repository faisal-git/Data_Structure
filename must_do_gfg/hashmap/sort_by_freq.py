#https://practice.geeksforgeeks.org/problems/sorting-elements-of-an-array-by-frequency/0/
# code is O(n^2) when freq of all elements is 1
import collections
import heapq
'''for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    freq=collections.Counter(arr)
    print(*sorted(arr,reverse=True,key=lambda i: (freq[i],-i)))'''
# using heap
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    freq=collections.Counter(arr)
    q=[]
    for val in freq.keys():
        heapq.heappush(q,[-freq[val],val])
    res=[]
    while q:
        r,val=heapq.heappop(q)
        res.extend([val]*abs(r))
    print(*res)
        