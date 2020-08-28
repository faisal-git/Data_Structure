# https://practice.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1

def maxLen(n, arr):
    #Code here
    cache={}
    _sum=0
    res=0
    for i,val in enumerate(arr):
        _sum+=val
        if _sum==0:
            res=i+1
        
        elif _sum in cache:
            res=max(res,i-cache[_sum])
        else:
            cache[_sum]=i
    return res
