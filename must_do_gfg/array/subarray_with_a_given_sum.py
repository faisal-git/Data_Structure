# https://practice.geeksforgeeks.org/problems/subarray-with-given-sum/0
# brute force is to travel through all it subarray and find the answer . Time: O(N^2) and space is O(1)
# other efficient way to solve is using cache.
# takes O(N) time and space 
for _ in range(int(input())):
    n,target=map(int,input().split())
    arr=list(map(int,input().split()))
    res=[-1]
    _sum=0
    cache={0:-1}
    for i,val in enumerate(arr):
        if val==target:
            res=[i+1,i+1]
            break
        _sum+=val
        if _sum-target in cache:
            res=[cache[_sum-target]+2,i+1]
            break
        cache[_sum]=i
    print(*res)
    