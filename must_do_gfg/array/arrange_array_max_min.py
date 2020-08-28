
# using each index to store two values 
# remainder with max ele gives orignal value
# quotient gives reqired value
# at even position storing curr max
# at odd position storing curr min
# arr[i]%mval gives the value sotred previously
# arr[i]//mval gives the required value
# ex: lets say u want to store two values 5,10 at a position where 10 reside 
# this can be done by taking any value greater then both letsay mval
# then add new=5*mval+10 and store it where 10 reside 
# new%mval gives 10 and new//mval gives 5(other value)
# code
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    _max,_min=n-1,0
    mval=arr[_max]+1 # stores max value
    for i in range(n):
        if i%2:
            arr[i]+=(arr[_min]%mval)*mval
            _min+=1
        else:
            arr[i]+=(arr[_max]%mval)*mval
            _max-=1
    for i in range(n):
        arr[i]//=mval
    print(*arr)