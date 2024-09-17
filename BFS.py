from collections import deque

# Function to perform BFS
def bfs(graph, start_node):
    visited = set()  # Set to keep track of visited nodes
    queue = deque([start_node])  # Queue to manage the frontier
    bfs_order = []  # List to store the order of nodes visited

    while queue:
        node = queue.popleft()  # Remove the node from the front of the queue
        
        if node not in visited:
            visited.add(node)  # Mark the node as visited
            bfs_order.append(node)  # Add the node to the BFS order list
            
            # Add all unvisited adjacent nodes to the queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    
    return bfs_order

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = 'A'
bfs_result = bfs(graph, start_node)
print("Breadth-First Search order:", bfs_result)
