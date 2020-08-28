# https://practice.geeksforgeeks.org/problems/common-elements/0/
# Time is O(max(length)) and space is O(max(length))
for _ in range(int(input())):
    lengths=list(map(int,input().split()))
    take_input=lambda: set(map(int,input().split()))
    a=list(map(int,input().split()))
    b,c=take_input(),take_input()
    res=[]
    prev=float('inf')
    for val in a:
        if val==prev:continue
        else:
            if val in b and val in c:
                res.append(val)
            
            prev=val
            
    if res:
        print(*res)
    else:
        print(-1)