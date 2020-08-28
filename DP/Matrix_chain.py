# for reff: http://www.personal.kent.edu/~rmuhamma/Algorithms/MyAlgorithms/Dynamic/chainMatrixMult.htm
# to minimize the total numbet of scalar multiplication to in order to multiply n matrix
# OPitmal substructure :
#                       lets says we have n matrices ,so there are n-1 ways we can divide it into two parts 
# for ex: lets we decided to multiple first 4 matrices seprately and rest n-4 seperately and further 
# after solving subproblems for n=4 and n=n-4 optimally we can combine the resutlt for the global optimal .
# since to arrive at the global optimal solution we need to compute optimal solution smaller subproblems
# this problems exhibits optimal substructure .
# how to proof Oerlapping subproblems: https://www.geeksforgeeks.org/matrix-chain-multiplication-dp-8/
# hecne dp will be benificial here.
# dp[i][j] min. scalar multiplication required to multiply ith to jth matrices which appears in sequence of matrices to be multiplited
# input format: Input: p[] = {10, 20, 30, 40, 30} 
# interpretation : There are 4 matrices of dimensions 10x20,20x30, 30x40 and 40x30.

# Top Down: Time O(N^3) since we n^2 possible combination of i,j and for each i,j pair 
def mcm(i,j,p,dp):
    if i==j:
        return 0
    if i==j-1:
        return p[i-1]*p[i]*p[j]
    if dp.get((i,j)):
        return dp[(i,j)]
    lcl_min=float('inf')
    for k in range(i,j):
        lcl_min=min(mcm(i,k,p,dp)+mcm(k+1,j,p,dp)+p[i-1]*p[k]*p[j],lcl_min)
    dp[(i,j)]=lcl_min
    return lcl_min
# to check correctness print(mcm(1,4,[10, 20, 30, 40, 30],{}))
# bottom is the solution is little tricky >
# dp[i][j]=min cost of muliplying matrix i to j inlcusive 
# for instance to compute dp[1][3] we need dp[1][1],dp[1][2],dp[2][3],dp[3][3] to be solved previously
# hece we loop in reverse order starting from n-2 for i ,which set lower bounary of matrix to be inlcuded
# inner loop starts form i+1 since i==j then its 0 ,j defines the upper boundary of matrix to be included 
# innnermost loop(K) start from i and goes all the way upto j-1 try all possible partition and calulating min cost 

def mcm(p): 
    n=len(p)
    dp=[[0]*n for _ in range(n)]

    for i in range(n-2,0,-1):
        for j in range(i+1,n,1):
            dp[i][j]=float('inf')
            for k in range(i,j):
                dp[i][j]=min(dp[i][j],dp[i][k]+dp[k+1][j]+p[i-1]*p[k]*p[j])
    return (dp[1][n-1])

# standard Bottom up solution solution 

def mcm(p):
    n=len(p)
    dp=[[0]*n for _ in range(n)]
    for L in range(2,n):
        for i in range(1,n-L+1):
            j=i+L-1
            dp[i][j]=float('inf')
            for k in range(i,j):
                dp[i][j]=min(dp[i][j],dp[i][k]+dp[k+1][j]+p[i-1]*p[k]*p[j])
    return (dp[1][n-1])
                
print(mcm([10, 20, 30, 40, 30]))