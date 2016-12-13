# 6.00 Problem Set 11
#
# graph.py
#
# A set of data structures to represent graphs
#

BAD_EDGE_MSG = "Total distance outdoors cannot exceed the total "+\
                "distance of the route"

class Node(object):
   def __init__(self, name):
       self.name = str(name)
   def getName(self):
       return self.name
   def __str__(self):
       return self.name
   def __repr__(self):
      return self.name
   def __eq__(self, other):
      return self.name == other.name
   def __ne__(self, other):
      return not self.__eq__(other)

class Edge(object):
   def __init__(self, src, dest):
       self.src = src
       self.dest = dest
   def getSource(self):
       return self.src
   def getDestination(self):
       return self.dest
   def reverse(self):
       return Edge(self, self.dest, self.src)
   def __str__(self):
       return str(self.src) + '->' + str(self.dest)

class Route(Edge):
    def __init__(self, src, dest, total_dist, dist_outdoors):
        self.src = src
        self.dest = dest
        if dist_outdoors > total_dist:
            raise ValueError(BAD_EDGE_MSG)
        self.total_dist = total_dist
        self.dist_outdoors = dist_outdoors

class Digraph(object):
   """
   A directed graph
   """
   def __init__(self):
       self.nodes = set([])
       self.edges = {}
   def addNode(self, node):
       if node in self.nodes:
           raise ValueError('Duplicate node')
       else:
           self.nodes.add(node)
           self.edges[node] = []
   def addEdge(self, edge):
       src = edge.getSource()
       dest = edge.getDestination()
       if not(src in self.nodes and dest in self.nodes):
           raise ValueError('Node not in graph')
       self.edges[src].append(dest)
   def childrenOf(self, node):
       print 'Parameter type:', type(node)
       print 'Key type:', type(self.edges.keys()[0])
       print 'Node in keys:', node in self.edges.keys()
       return self.edges[node]
   def hasNode(self, node):
       return node in self.nodes
   def __str__(self):
       res = ''
       for k in self.edges:
           for d in self.edges[k]:
               res = res + str(k) + '->' + str(d) + '\n'
       return res[:-1]

class Graph(Digraph):
    """
    A graph with both directed and bidirectional edges.
    """
    def addBidirectionalEdge(self, edge):
        super(Graph, self).addEdge(edge)
        super(Graph, self).addEdge(edge.reverse())

