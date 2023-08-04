def dijkstra(graph, start, target):
    # Init bhhialize distances to all nodes as infinity except the start node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Keep track of visited nodes
    visited = set()  # new add

    # Keep track of previous nodes in the shortest path
    previous = {node: None for node in graph}

    while len(visited) < len(graph):
        # Find the node with the minimum distance from the start node
        min_distance = float('inf')
        current_node = None
        for node in graph:
            if node not in visited and distances[node] < min_distance:
                min_distance = distances[node]
                current_node = node

        if current_node is None:
            break

        # Mark the current node as visited
        visited.add(current_node)

        # Update distances to its neighbors
        for neighbor, weight in graph[current_node].items():
            new_distance = distances[current_node] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current_node

    # Calculate the distance of the shortest path
    shortest_distance = distances[target]

    # Backtrack to find the shortest path from 'A' to the target node
    path = [target]
    while previous[target] is not None:
        target = previous[target]
        path.insert(0, target)

    return shortest_distance, path

# Example graph represented as an adjacency dictionary
graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'A': 2, 'C': 1, 'D': 7},
    'C': {'A': 4, 'B': 1, 'D': 3},
    'D': {'B': 7, 'C': 3}
}

start_node = 'A'
target_node = 'D'
shortest_distance, shortest_path = dijkstra(graph, start_node, target_node)

print("Shortest distance from node {} to node {}: {}".format(start_node, target_node, shortest_distance))
print("Shortest path from node {} to node {}: {}".format(start_node, target_node, shortest_path))
