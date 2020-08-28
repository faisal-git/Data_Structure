# https://practice.geeksforgeeks.org/problems/largest-number-formed-from-an-array/0/

# can be solved using merge sort 
# int(arr[index]+arr[j])<int(arr[j]+arr[index]) comparing number at index and j

for _ in range(int(input())):
    n=int(input())
    arr=list(input().split())
    for i in range(n-1):
        index=i
        for j in range(i+1,n):
            if int(arr[index]+arr[j])<int(arr[j]+arr[index]):
                index=j
        arr[i],arr[index]=arr[index],arr[i]
    #print(arr)
    print(''.join(arr))
                
            