def find_mst(graph):
    # sort the edges in the graph by weight in ascending order
    edges = graph.edges
    edges.sort_by_weight()

    # create a disjoint-set data structure to keep track of which vertices
    # are already in the MST
    disjoint_set = create_disjoint_set(graph.vertices)

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
