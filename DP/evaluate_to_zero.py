#https://www.interviewbit.com/problems/evaluate-expression-to-true/
# Bottom up is crucial and tricky
# Top Down
t_cache,f_cache={},{}
def solve(i,j,s,isTrue):
    #print(i,j,isTrue)
    if i==j:
        if isTrue and s[i]=='T':
            return 1
        elif not isTrue and s[i]=='F':
            return 1
        else:
            return 0
    if isTrue and t_cache.get((i,j)):
        return t_cache[(i,j)]
    if not isTrue and f_cache.get((i,j)):
        return f_cache[(i,j)]
    ans=0
    for k in range(i+1,j,2):
        if isTrue:
            if s[k]=='&':
                ans+=   solve(i,k-1,s,True)*solve(k+1,j,s,True)
            elif s[k]=='|':
                ans+=   solve(i,k-1,s,True)*solve(k+1,j,s,True)     +   solve(i,k-1,s,True)*solve(k+1,j,s,False)    + solve(i,k-1,s,False)*solve(k+1,j,s,True)
            else:
                ans+=   solve(i,k-1,s,True)*solve(k+1,j,s,False)    +   solve(i,k-1,s,False)*solve(k+1,j,s,True)

        else:
            if s[k]=='&':
                ans+=   solve(i,k-1,s,False)*solve(k+1,j,s,False)   +   solve(i,k-1,s,True)*solve(k+1,j,s,False)    +   solve(i,k-1,s,False)*solve(k+1,j,s,True)
                
            elif s[k]=='|':
                 ans+=  solve(i,k-1,s,False)*solve(k+1,j,s,False)
                
            else:
                ans+=   solve(i,k-1,s,True)*solve(k+1,j,s,True)     +   solve(i,k-1,s,False)*solve(k+1,j,s,False)
    if isTrue:
        t_cache[(i,j)]=ans
    else:
        f_cache[(i,j)]=ans
    return ans
            

#exp="T|T&F^T"
exp='T^T^T^F|F&F^F|T^F^T'
print(solve(0,len(exp)-1,exp,True))
    