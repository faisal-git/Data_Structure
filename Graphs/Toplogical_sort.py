# course taken with pre-requisites
# program buid dependencies
# can be done using BFS,DFS,and kahn's algorithm
# https://leetcode.com/problems/course-schedule-ii/


def detect_cycle(node,visited,visiting):
    visited[node]=True
    visiting[node]=True
    for adj in graph[node]:
        if (not visited[adj]) and (detect_cycle(adj,visited,visiting)):
            return True
        elif(visiting[adj]):
            return True
    visiting[node]=False
    return False

def topological_sort(node):
            
    for adj in graph[node]:
        if(not visited[adj]):
            topological_sort(adj)
    ans.append(node)
    visited[node]=True

def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        def topological_sort(node):
            
            for adj in graph[node]:
                if(not visited[adj]):
                    topological_sort(adj)
            ans.append(node)
            visited[node]=True
            
        
        
        
        
    
        graph=collections.defaultdict(list)
        for each in prerequisites:
            graph[each[1]].append(each[0])
            
        visited=[False]*numCourses
        visiting=[False]*numCourses
        
        for c in range(numCourses):
            if(not visited[c])and (detect_cycle(c)):
                return []
        visited=[False]*numCourses
        ans=[]
        for t in range(numCourses):
            if(not visited[t]):
                topological_sort(t)
        ans.reverse()
        return ans
            