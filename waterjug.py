from collections import deque
def water_jug_solver(jug1, jug2, target):
    visited = set()
    q = deque()
    q.append((0, 0))
    while q:
        curr_jug1, curr_jug2 = q.popleft()
        if curr_jug1 == target or curr_jug2 == target:
            print(f"Solution found: Jug1 = {curr_jug1}, Jug2 = {curr_jug2}")
            return True
        if (curr_jug1, curr_jug2) in visited:
            continue
        visited.add((curr_jug1, curr_jug2))
        next_states = [
            (jug1, curr_jug2),
            (curr_jug1, jug2),
            (0, curr_jug2),
            (curr_jug1, 0),
            (max(0, curr_jug1 - (jug2 - curr_jug2)), min(jug2, curr_jug2 + curr_jug1)),
            (min(jug1, curr_jug1 + curr_jug2), max(0, curr_jug2 - (jug1 - curr_jug1)))
        ]
        for state in next_states:
            if state not in visited:
                q.append(state)
    print("No solution found.")
    return False
def main():
    jug1_capacity = 4
    jug2_capacity = 3
    target = 2
    water_jug_solver(jug1_capacity, jug2_capacity, target)
if __name__ == "__main__":
    main()
