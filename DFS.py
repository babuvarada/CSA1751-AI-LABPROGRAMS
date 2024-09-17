# Function to perform DFS recursively
def dfs(graph, start_node, visited=None):
    if visited is None:
        visited = set()  # Initialize the visited set
    
    visited.add(start_node)  # Mark the current node as visited
    dfs_order.append(start_node)  # Store the DFS traversal order

    # Visit all the adjacent nodes that haven't been visited yet
    for neighbor in graph[start_node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    
    return dfs_order

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
dfs_order = []  # List to store the DFS order
dfs_result = dfs(graph, start_node)
print("Depth-First Search order:", dfs_result)
