#AI7: 8 tiles - Hill Climbing

import random
import copy

# Define goal state
goal_state = [[1,2,3],[4,5,6],[7,8,0]]

# Define Manhattan distance heuristic
def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                continue
            row, col = divmod(state[i][j]-1, 3)
            distance += abs(row - i) + abs(col - j)
    return distance

# Define hill climbing algorithm function
def hill_climbing(start_state, h):
    current_state = start_state
    current_h = h(current_state)
    while True:
        print("Current state (h = " + str(current_h) + "):")
        for row in current_state:
            print(row)
        neighbors = []
        for i in range(3):
            for j in range(3):
                if current_state[i][j] == 0:
                    # Move blank space up
                    if i > 0:
                        neighbor = copy.deepcopy(current_state)
                        neighbor[i][j], neighbor[i-1][j] = neighbor[i-1][j], neighbor[i][j]
                        neighbors.append(neighbor)
                    # Move blank space down
                    if i < 2:
                        neighbor = copy.deepcopy(current_state)
                        neighbor[i][j], neighbor[i+1][j] = neighbor[i+1][j], neighbor[i][j]
                        neighbors.append(neighbor)
                    # Move blank space left
                    if j > 0:
                        neighbor = copy.deepcopy(current_state)
                        neighbor[i][j], neighbor[i][j-1] = neighbor[i][j-1], neighbor[i][j]
                        neighbors.append(neighbor)
                    # Move blank space right
                    if j < 2:
                        neighbor = copy.deepcopy(current_state)
                        neighbor[i][j], neighbor[i][j+1] = neighbor[i][j+1], neighbor[i][j]
                        neighbors.append(neighbor)
        if not neighbors:
            # Reached local minimum, return current state
            return current_state
        best_neighbor = min(neighbors, key=h)
        best_neighbor_h = h(best_neighbor)
        if best_neighbor_h >= current_h:
            # Reached local minimum, return current state
            return current_state
        current_state = best_neighbor
        current_h = best_neighbor_h

# Define initial state
start_state = [[0, 1, 3], [4, 2, 5], [7, 8, 6]]

# Solve 8-puzzle problem with hill climbing algorithm
solution = hill_climbing(start_state, manhattan_distance)

# Print solution
print("Initial state:")
for row in start_state:
    print(row)
print("\nSolution:")
for row in solution:
    print(row)