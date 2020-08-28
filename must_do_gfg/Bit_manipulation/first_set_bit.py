# 
for _ in range(int(input())):
    num=int(input())
    if num:
        cnt=1
        while num:
            if num&1:
                break
            else:
                cnt+=1
                num>>=1
        print(cnt)
            
        
    else:
        print(0)