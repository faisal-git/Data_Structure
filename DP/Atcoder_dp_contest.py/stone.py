# why dp ?
# to know the ans for k number of stone you need to have k-a1 ,k-a2 ,k-a(n) ,this optimal substructure
# k (no of stone ) is the only dp state here  and dp[k] represent for given stones whthter first will or not
# at every step we need to take decision of chosing ai such from there ther would be no way win for second guy
# for given k if there exist at least one way k-a (a can any value form list) from where there is no way to win ,then first guy will win for k
# there is clear overlapping subprobems.
# code
# Time : O(k*n) space: O(K)
# bottom up method
n,k=map(int,input().split())
steps=list(map(int,input().split()))
dp=[True]*(k+1)
dp[0]=False
for stone in range(1,k+1):
  for s in steps:
    if s<=stone:
      dp[stone]=dp[stone]and dp[stone-s]
    else:
      break
  dp[stone]=not dp[stone]
#print(dp)
if dp[k]:
  print('First')
else:
  print('Second')