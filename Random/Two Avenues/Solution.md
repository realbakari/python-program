This problem can be solved by finding a minimum spanning tree (MST) of the given graph, and then choosing the two most expensive edges in the MST as the two avenues.

A minimum spanning tree is a subset of the edges of a connected, undirected graph that connects all the vertices together, without any cycles and with the minimum possible total edge weight. In this problem, the minimum spanning tree can be found using the well-known Kruskal's algorithm.

Once the minimum spanning tree has been found, the two most expensive edges in the tree can be chosen as the two avenues. The cost of each edge in the MST represents the number of tugriks that the citizens will have to pay if that edge is chosen as an avenue. Therefore, by choosing the two most expensive edges, we can maximize the number of tugriks that the citizens will have to pay.

To find the two most expensive edges in the MST, we can simply sort the edges by weight and choose the first two edges in the sorted list. The first edge will be the most expensive edge, and the second edge will be the second most expensive edge.

After finding the two most expensive edges, we can print the total number of tugriks that the citizens will have to pay, followed by the details of the two chosen avenues.

*Note* that this solution assumes that the given graph is connected, i.e., there is a path between any two vertices in the graph. This is a valid assumption, because the problem statement guarantees that you can get from any crossroad to any other by moving only along the streets.



This implementation of the solution is correct and efficient, because it uses the Kruskal's algorithm to find the minimum spanning tree in O(m log m) time, where m is the number of edges in the graph. Sorting the edges in the MST by weight takes O(m log m) time as well, so the overall time complexity of the solution is O(m log m).

Note that we are using the weight of each edge in the MST as the cost that the citizens will have to pay if that edge is chosen as an avenue. This is a valid approach, because the weight of each edge in the MST represents the minimum cost of reaching one vertex from the other along the path that includes that edge. Therefore, if we choose that edge as an avenue, the citizens will have to pay the cost represented by the weight of the edge.

Since the time complexity of the solution is O(m log m), it can handle large graphs with up to 500,000 edges and vertices,

