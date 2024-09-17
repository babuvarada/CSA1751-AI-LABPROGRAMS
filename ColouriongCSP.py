class MapColoring:
    def __init__(self, graph, colors):
        self.graph = graph
        self.colors = colors
        self.color_assignment = {}

    def is_valid(self, node, color):
        for neighbor in self.graph[node]:
            if neighbor in self.color_assignment and self.color_assignment[neighbor] == color:
                return False
        return True

    def solve(self):
        return self.backtrack()

    def backtrack(self):
        if len(self.color_assignment) == len(self.graph):
            return True
        node = self.select_unassigned_node()
        for color in self.colors:
            if self.is_valid(node, color):
                self.color_assignment[node] = color
                if self.backtrack():
                    return True
                del self.color_assignment[node]
        return False

    def select_unassigned_node(self):
        for node in self.graph:
            if node not in self.color_assignment:
                return node
        return None

    def get_solution(self):
        return self.color_assignment

graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'C', 'E'],
    'C': ['A', 'B', 'D', 'F'],
    'D': ['A', 'C', 'G'],
    'E': ['B', 'F'],
    'F': ['C', 'E', 'G'],
    'G': ['D', 'F']
}
colors = ['Red', 'Green', 'Blue']

map_coloring = MapColoring(graph, colors)
if map_coloring.solve():
    print(map_coloring.get_solution())
else:
    print("No solution exists")
