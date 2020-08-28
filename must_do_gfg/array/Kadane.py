# https://practice.geeksforgeeks.org/problems/kadanes-algorithm/0
# Time O(N) and O(1) space. 
# application of DP 
#code
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    max_sum=float('-inf')
    curr=0
    for val in arr:
        curr=max(val,curr+val)
        max_sum=max(curr,max_sum)
    print(max_sum)