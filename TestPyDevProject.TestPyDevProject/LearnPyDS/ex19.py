'''
Created on Jan 2, 2019

@author: nwijesinha

This exercise is to create graphs using Python
A graph is pictorial representaiton of a set of object where some pairs of the objects are connected by link
Following are the basic operations perfomed on graphs
    Display graph vertices, display graph edges, add a vertexx, add an edge and creating a graph
A graph can be created using Python dictionary data types

'''


class graph:

    # create class constructor
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = []
        self.gdict = gdict

    # get the keys of the dictionary
    def getVertices(self):
        return list(self.gdict.keys())
    
    # Defin fucntion for edges
    def edges(self):
        return self.findedges()

    # Define function to find the distinct edges
    def findedges(self):
        edgename = []
        for vrtx in self.gdict:
            for nxtvrtx  in self.gdict[vrtx]:
                if{nxtvrtx, vrtx} not in edgename:
                    edgename.append({vrtx, nxtvrtx})
        return edgename
    
    # define a function to add a vetiex as a key
    def addVertex(self, vrtx):
        if vrtx not in self.gdict:
            self.gdict[vrtx] = []
            
    # define a function to add a new edge
    def addEdge(self, edge):
        edge = set(edge)
        (vrtx1, vrtx2) = tuple(edge)
        if vrtx1 in self.gdict:
            self.gdict[vrtx1].append(vrtx2)
        else:
            self.gdict[vrtx1] = [vrtx2]
        
        
# Create a variabl dictioanry with graph elements
graph_elements = {"a" : ["b", "c"],
         "b" : ["a", "d"],
         "c" : ["a", "d"],
         "d" : ["e"],
         "e" : ["d"]
         }

# Create a graph 

g = graph(graph_elements)

# print graph vertices
print("Printing graph vertices")
print(g.getVertices())

# print graph edges
print("Printing graph edges")
print(g.edges())

# adding vertex f
g.addVertex("f")

# print graph vertices after adding f
print("Printing graph vertices after adding f")
print(g.getVertices())

g.addEdge({'a', 'e'})
g.addEdge({'a', 'c'})

# print graph edges after adding {'a', 'e'} and {'a', 'c'}
print("Printing graph edges after adding {'a', 'e'} and {'a', 'c'}")
print(g.edges())

