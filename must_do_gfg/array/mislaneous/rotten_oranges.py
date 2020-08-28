# https://leetcode.com/problems/rotting-oranges/
# https://practice.geeksforgeeks.org/problems/rotten-oranges/0
# the idea is simple BFS traversal from all point of rotten oranges
# and further including only those cell which is being rotten by any of currently rotten oranges present is stack
# Time O(r*c) and same is the space
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time=0
        row,col=len(grid),len(grid[0])
        rotten,fresh=collections.deque(),0
        for i in range(row):
            for j in range(col):
                if grid[i][j]==2:
                    rotten.append((i,j))
                if grid[i][j]==1:
                    fresh+=1
        r_vector=[1,-1,0,0]
        c_vector=[0,0,1,-1]
        while fresh and rotten:
            flag=False
           # new_rotten=set()
            for _ in range(len(rotten)):
                r,c=rotten.popleft()
                for i in range(4):
                    temp_r,temp_c=r+r_vector[i],c+c_vector[i]
                    if temp_r>=0 and temp_c>=0 and temp_r<row and temp_c<col and grid[temp_r][temp_c]==1:
                        rotten.append((temp_r,temp_c))
                        grid[temp_r][temp_c]=2
                        flag=True
                        fresh-=1
            if flag:
                time+=1
        return -1 if fresh else time
                    
    