import heapq

def astar(start, goal, graph):
    """
    A* search algorithm implementation.

    Parameters:
    start (node): The starting node for the search.
    goal (node): The goal node to find.
    graph (dict): A dictionary representation of the graph.

    Returns:
    path (list): A list of nodes representing the path from the start node to the goal node.
    distance (int): The distance from the start node to the goal node.
    """
    # Initialize variables
    visited = set()
    heap = [(0, start)]
    distances = {start: 0}
    path = {start: None}

    # A* search algorithm
    while heap:
        (cost, current) = heapq.heappop(heap)

        if current == goal:
            # Reconstruct the path from the start node to the goal node
            distance = distances[current]
            path_list = []
            while current is not None:
                path_list.append(current)
                current = path[current]
            path_list.reverse()
            return path_list, distance

        visited.add(current)

        # Check neighbors
        for neighbor, cost in graph[current].items():
            if neighbor in visited:
                continue
            heuristic_cost = cost + distances[current]
            if neighbor not in distances or heuristic_cost < distances[neighbor]:
                distances[neighbor] = heuristic_cost
                priority = heuristic_cost + heuristic(neighbor, goal)
                heapq.heappush(heap, (priority, neighbor))
                path[neighbor] = current

    return None, None


def heuristic(current, goal):
    """
    A* search heuristic function.

    Parameters:
    current (node): The current node in the search.
    goal (node): The goal node to find.

    Returns:
    The estimated distance from the current node to the goal node.
    """
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

graph = {
    'A': {'B': 5, 'C': 1},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 1, 'B': 2, 'D': 4},
    'D': {'B': 1, 'C': 4}
}


print("hell");
start = 'A'
goal = 'D'

path, distance = astar(start, goal, graph)
print(f"Path: {path}")
print(f"Distance: {distance}")
