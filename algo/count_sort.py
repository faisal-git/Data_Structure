# https://practice.geeksforgeeks.org/problems/largest-even-number/0

"""For simplicity, consider the data in the range 0 to 9. 
Input data: 1, 4, 1, 2, 7, 5, 2
  1) Take a count array to store the count of each unique object.
  Index:     0  1  2  3  4  5  6  7  8  9
  Count:     0  2  2  0   1  1  0  1  0  0

  2) Modify the count array such that each element at each index 
  stores the sum of previous counts. 
  Index:     0  1  2  3  4  5  6  7  8  9
  Count:     0  2  4  4  5  6  6  7  7  7

#cummulative count simple means highest index where 2 appear when we deal with 1 based indexing

The modified count array indicates the position of each object in 
the output sequence.
 
  3) Output each object from the input sequence followed by 
  decreasing its count by 1.
  Process the input data: 1, 4, 1, 2, 7, 5, 2. Position of 1 is 2.
  Put data 1 at index 2 in output. Decrease count by 1 to place 
  next data 1 at an index 1 smaller than this index"""
# given a number print largest possible even number by rearranging its digit
# for ex: 1432 ans is 4312
# approach is to sort all digits using count sort (n+v) ,here n is the length of number and v is 9, since single digit range 0-9
# let say it store sorted list in arr ,
# the find the sorted even and place it at index 0 
# reverse and combine the elements for arr to get result.
for _ in range(int(input())):
    num=input()
    cnt=[0]*10
    for val in num:
        cnt[int(val)]+=1
    for i in range(1,10):
        cnt[i]+=cnt[i-1]
    arr=[0]*len(num)
    for val in num:
        arr[cnt[int(val)]-1]=val
        cnt[int(val)]-=1
    for i,val in enumerate(arr):
        if int(val)%2==0:
            temp=val
            j=i
            while j>0: 
                arr[j]=arr[j-1]
                j-=1
            arr[0]=temp
            break
    #print(arr)
    print(int("".join(arr[::-1])))
        