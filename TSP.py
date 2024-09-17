import itertools

def calculate_path_length(path, distances):
    length = 0
    for i in range(len(path) - 1):
        length += distances[path[i]][path[i+1]]
    length += distances[path[-1]][path[0]]
    return length

def traveling_salesman_problem(distances):
    n = len(distances)
    shortest_path = None
    min_length = float('inf')
    for path in itertools.permutations(range(n)):
        length = calculate_path_length(path, distances)
        if length < min_length:
            min_length = length
            shortest_path = path
    return shortest_path, min_length

distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

path, length = traveling_salesman_problem(distances)
print("Shortest path:", path)
print("Length of the path:", length)
