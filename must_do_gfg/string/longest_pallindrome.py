# https://practice.geeksforgeeks.org/problems/longest-palindrome-in-a-string/0/
# checking for every character ,a pallindrome includig that is character can be how long
# a character can be a part of a pallindrome in two ways 
# 1. as a centre of odd length pallidrom
# 2. or as a part of even length pallidrome 

def pallindrome(i,j,s):
    n=len(s)
    while i>=0 and j<n:
        if s[i]!=s[j]:
            break
        i-=1
        j+=1
    return i,j

for _ in range(int(input())):
    res=[-1,1]
    s=input()
    for k in range(len(s)-1):
        
        '''
        this code can be used to remove repeating code snippet ,
        for m,n in ((k-1,k+1),(k,k+1)):
            i,j=pallindrome(m,n,s)
            if j-i>res[1]-res[0]:
                res[1]=j
                res[0]=i'''
            
           
        i,j=pallindrome(k-1,k+1,s)
        if j-i>res[1]-res[0]:
            res[1]=j
            res[0]=i
        i,j=pallindrome(k,k+1,s)
        if j-i>res[1]-res[0]:
            res[1]=j
            res[0]=i
    print(s[res[0]+1:res[1]])