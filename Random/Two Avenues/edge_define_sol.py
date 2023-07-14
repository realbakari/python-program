class Edge:
    def __init__(self, vertex1, vertex2, weight):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.weight = weight


class Graph:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges


class DisjointSet:
    def __init__(self, vertices):
        self.parents = {}
        self.ranks = {}
# initialize the disjoint-set data structure with singleton sets
# for each vertex in the graph
    for vertex in vertices:
        self.parents[vertex] = vertex
        self.ranks[vertex] = 0

def find(self, vertex):
    # find the root of the set that the given vertex belongs to
    if self.parents[vertex] != vertex:
        self.parents[vertex] = self.find(self.parents[vertex])
    return self.parents[vertex]

def union(self, set1, set2):
    # find the roots of the sets that the given vertices belong to
    root1 = self.find(set1)
    root2 = self.find(set2)

    # if the sets are already in the same connected component,
    # there is nothing to do
    if root1 == root2:
        return

    # merge the smaller set into the larger set, based on their ranks
    if self.ranks[root1] < self.ranks[root2]:
        self.parents[root1] = root2
    elif self.ranks[root1] > self.ranks[root2]:
        self.parents[root2] = root1
    else:
        self.parents[root1] = root2
        self.ranks[root2] += 1

def find_mst(graph):
# sort the edges in the graph by weight in ascending order
    edges = graph.edges
    edges.sort(key=lambda e: e.weight)

    # create a disjoint-set data structure to keep track of which vertices
# are already in the MST
disjoint_set = DisjointSet(graph.vertices)

# initialize the minimum spanning tree as an empty list of edges
mst = []

# iterate over the edges in the sorted list
for edge in edges:
    # find the connected components that the edge's vertices belong to
    component1 = disjoint_set.find(edge.vertex1)
    component2 = disjoint_set.find(edge.vertex2)

    # if the edge's vertices belong to different connected components,
    # add the edge to the MST and merge the two components
    if component1 != component2:
        mst.append(edge)
        disjoint_set.union(component1, component2)

    return mst

# read the number of test cases
num_tests = int(input())

# iterate over the test cases
for _ in range(num_tests):
    # read the number of crossroads and streets
    n, m = map(int, input().split())

    # read the list of vertices and edges
vertices = range(1, n + 1)
edges = []
for _ in range(m):
    u, v = map(int, input().split())
    edges.append(Edge(u, v, 1))

# create a graph with the given vertices and edges
graph = Graph(vertices, edges)

# find the minimum spanning tree of the graph
mst = find_mst(graph)

# sort the edges in the MST by weight in descending order

# choose the two most expensive edges as the two avenues
mst.sort(key=lambda e: -e.weight)
avenue1 = mst[0]
avenue2 = mst[1]

# calculate the total cost of the two avenues
total_cost = avenue1.weight + avenue2.weight

# print the total cost and the details of the two avenues
print(total_cost)
print(avenue1.vertex1, avenue1.vertex2)
print(avenue2.vertex1, avenue2.vertex2)

