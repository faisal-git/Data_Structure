
# https://practice.geeksforgeeks.org/problems/count-the-triplets/0
# trival brute force way of doing this is to 3 nested for loop . Time O(N^3)
# sorting and checking for every number in list whether there is any pair whose sum is equal to that number.
# the later part can be achieved either by two sum technique or using two pointer
# other way is to test each pair sum and check if it exits in the list .
# Time O(N^2)



for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    targets=set(arr)
    cnt=0
    for i in range(n-1):
        for j in range(i+1,n):
            if i==j: continue
            if arr[i]+arr[j] in targets:
                cnt+=1
    if cnt:
        print(cnt)
    else:
        print(-1)