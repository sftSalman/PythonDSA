def find_min_edge(edges) :
    # Helper function to find the edge with the minimum weight
    min_weight = float ( 'inf' )
    min_edge = None
    for edge, weight in edges.items () :
        if weight < min_weight :
            min_weight = weight
            min_edge = edge
    return min_edge, min_weight


def prim(graph, start, target) :
    # Initialize the minimum spanning tree and visited nodes
    mst = {}
    visited = set ()

    while len ( mst ) < len ( graph ) :
        # Find the edges from the current node to its neighbors
        edges = {neighbor : weight for neighbor, weight in graph[start].items () if neighbor not in visited}

        if not edges :
            break

        # Find the edge with the minimum weight
        min_edge, min_weight = find_min_edge ( edges )

        # Add the edge to the minimum spanning tree
        mst[min_edge] = min_weight
        visited.add ( start )

        # Move to the next node with the minimum weight edge
        start = min_edge

    return mst


# Example graph represented as an adjacency dictionary
graph = {
    'A' : {'B' : 2, 'C' : 4},
    'B' : {'A' : 2, 'C' : 1, 'D' : 7},
    'C' : {'A' : 4, 'B' : 1, 'D' : 3},
    'D' : {'B' : 7, 'C' : 3}
}

start_node = 'A'
target_node = 'D'
minimum_spanning_tree = prim ( graph, start_node, target_node )

print ( "Minimum Spanning Tree from node {} to node {}:".format ( start_node, target_node ) )
print ( minimum_spanning_tree )
