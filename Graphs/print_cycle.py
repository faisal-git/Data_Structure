# color algorithm can be used 
# no self loop and parallel edges
# state 0: not visited ,state 1: currently in visiting loop ,state 2: completely visited
import collections

def dfs(v,visited,g,parent,cycle):
    visited[v]=1
    print(v)
    for n in g[v]:
        if visited[n]==0:
            parent[n]=v
            dfs(n,visited,g,parent,cycle)
        elif visited[n]==2:
            continue
            
        elif parent[v]!=n: # means there exist a back edge
            # here we can just back track to find the cycle formed when started form v and goes upto n
            # and used marker to color all node of cycle with a color 
            # every cycle would have its unique color
            # impart unique color we can have a golbal var color: whose value should is inceresed when we found and a cycle 
            
            print((v,n))
            cycle.append((v,n))
    visited[v]=2
    
            
            
            
def print_cycle(start,end,parent):
    temp=[]
    while start!=end:
        temp.append(start)
        start=parent[start]
    print("cycle is : ",temp+[start])




def build_graph():
    g=collections.defaultdict(list)
    vertex=int(input("Enter the number of vertex.: "))
    e=int(int(input(" Enter the number of edges: ")))
    for _ in range(e):
        u,v=map(int,input().split())
        g[u].append(v)
        g[v].append(u)
        
    visited=[0]*vertex
    parent=[-1]*vertex
    cycle=[]
    for v in range(vertex):
        if not visited[v]:
            dfs(v,visited,g,parent,cycle)
    print(parent)
    while cycle:
        s,e=cycle.pop()
        print_cycle(s,e,parent)
    
build_graph()  