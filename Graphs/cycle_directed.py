# coloring node with 0,1,2 is good for this purpose:
# every time we make to call iscylce() with v we check whether or not there is cycle where v particpates
# https://leetcode.com/problems/course-schedule/
def isycle(v,visited,g):
    visited[v]=1
    for n in g[v]:
        if n==0:
            if iscycle(n,visited,g):
                return True
        elif n==2:
            continue
        elif n==1:
            return True
    visited[v]=2
    return False