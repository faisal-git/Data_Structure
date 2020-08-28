# https://practice.geeksforgeeks.org/problems/missing-number-in-array/0
# the idea is simple to calculate the sum of given arrray
# apply n*(n+1)/2 for finding the sum of first n natural number 
# subtract arr sum from n natural number sum
# Time O(N) 

for _ in range(int(input())):
    n=int(input())
    print((n*(n+1))//2 - sum(list(map(int,input().split()))))