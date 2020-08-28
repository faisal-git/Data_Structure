# https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s/0
import collections
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    freq=collections.Counter(arr)
    #print(freq)
    for val in (0,1,2):
        if val in freq:
            print(*[val for _ in range(freq[val])],end=" ")
    print("") # to ensure results of different test cases is printed in new line