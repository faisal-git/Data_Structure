# https://practice.geeksforgeeks.org/problems/longest-common-prefix-in-an-array/0
# time is O(n*(max length of string))
for _ in range(int(input())):
    n=int(input())
    strings=list(input().split())
    lcf=strings[0]
    for s in strings[1:]:
        size=min(len(s),len(lcf))
        i=0
        while i<size and s[i]==lcf[i]:
            i+=1
        lcf=s[:i]
        if not lcf:
            break
    if lcf:
        print(lcf)
    else:
        print(-1)

