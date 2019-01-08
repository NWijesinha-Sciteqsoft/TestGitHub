'''
Created on Jan 7, 2019

@author: nwijesinha

This exercise is learning about Graph Traversal in Python
Breadth First Search
Breadth first search (BFS),this algorithm traverses a graph breadth ward motion 
and uses a queue to remember to get the next vertex to start a search, 
when a dead end occurs in any iteration.

'''
import collections as c


class graph:

    # define constructor for class
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

        
def bfs(graph, startnode):
    # Track the visited and unvisited nodes using queue
    seen, queue = set([startnode]), c.deque([startnode])
    while queue:
        vertex = queue.popleft()
        marked(vertex)
        for node in graph[vertex]:
            if node not in seen:
                seen.add(node)
                queue.append(node)

                
# define marked function to print
def marked(n):
    print(n)
    

# The graph dictionary
gdict = { "a" : set(["b", "c"]),
                "b" : set(["a", "d"]),
                "c" : set(["a", "d"]),
                "d" : set(["e"]),
                "e" : set(["a"])
                }

bfs(gdict, "a")
