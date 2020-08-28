# https://practice.geeksforgeeks.org/problems/recursively-remove-all-adjacent-duplicates/0/
# Recursively remove all adjacent duplicates
# output for mississipie answer is mpie
# but for missiiipie answer is mipie 
# Time is O(N^2)
# the idea is to remove all adj duplicates in one pass
# if the result any two pass is same that means no more adj duplicates is present.

def remove_duplicates(s):
    i,n=0,len(s)
    if n<2:
        return s
    res=""
    while i<n-1:
        if s[i]==s[i+1]:
            i+=1
            while i<n and s[i]==s[i-1]:
                i+=1
            continue
        else:
            res+=s[i]
            i+=1
    if i<n:
        res+=s[i]
            
    return res
    
for _ in range(int(input())):
    s=list(input())
    prev=0
    curr=s
    while prev!=curr:
        curr,prev=remove_duplicates(curr),curr
    print(curr)