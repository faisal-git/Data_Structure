In graph theory, the shortest path problem is the problem of finding a path between
two vertices (or nodes) in a graph such that the sum of the weights of its 
constituent edges is minimized.

The problem is also sometimes called the single-pair shortest path problem, to distinguish it from the following variations:

-The single-source shortest path problem, in which we have to find shortest paths 
    from a source vertex v to all other vertices in the graph.

-The single-destination shortest path problem, in which we have to find shortest 
    paths from all vertices in the directed graph to a single destination vertex v. 
    This can be reduced to the single-source shortest path problem by reversing the arcs in the directed graph.
-The all-pairs shortest path problem, in which we have to find shortest paths 
    between every pair of vertices v, v' in the graph.

unwieghted grpah(directed or undirected graph):
    BFS can be used where we start from source vertex .

weighted graph and directed graph.
    
                    

The most important algorithms for solving this problem are:

1. Dijkstra's algorithm solves the single-source shortest path problem with non-negative edge weight.
2. Bellman–Ford algorithm solves the single-source problem if edge weights may be negative.
3. A* search algorithm solves for single-pair shortest path using heuristics to try to speed up the search.
4. Floyd–Warshall algorithm solves all pairs shortest paths.

