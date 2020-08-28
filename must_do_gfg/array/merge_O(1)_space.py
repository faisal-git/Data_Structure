#code
for _ in range(int(input())):
    n,m=map(int,input().split())
    arr=list(map(int,input().split()))
    arr.extend(list(map(int,input().split())))
    arr.sort()
    print(*arr)
    #print(*arr[n:])
    