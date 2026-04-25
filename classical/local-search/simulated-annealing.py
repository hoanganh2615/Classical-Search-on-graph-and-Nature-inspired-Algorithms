import math
import random

def simulated_annealing(
    graph, heuristic, start,
    initial_temp=1000.0,
    cooling_rate=0.95,
    min_temp=1e-3,
    max_iter=1000,
    goal=None
):

    current = start
    path = [start]

    best_node = start
    best_score = heuristic[start]

    temp = initial_temp

    for _ in range(max_iter):

        if temp <= min_temp:
            break

        neighbors = graph.get(current, [])
        if not neighbors:
            break

        next_node, _ = random.choice(neighbors)

        h_current = heuristic[current]
        h_next = heuristic[next_node]

        delta = h_next - h_current

        if delta < 0 or random.random() < math.exp(-delta / temp):
            current = next_node
            path.append(current)

            if heuristic[next_node] < best_score:
                best_score = heuristic[next_node]
                best_node = next_node

        if goal and current == goal:
            break

        temp *= cooling_rate

    return best_node, path


def main():
    graph = {
    'A': [('B', 3), ('C', 4), ('D', 5)],
    'B': [('A', 3), ('C', 4), ('E', 5)],
    'C': [('A', 4), ('B', 4)],
    'D': [('A', 5)],
    'E': [('B', 5), ('F', 10), ('G', 12)],
    'F': [('E', 10)],
    'G': [('E', 12)]
    }
    
    heuristic = {
    'A': 10,
    'B': 8,
    'C': 9,
    'D': 11,
    'E': 3,
    'F': 1,
    'G': 0
    }
    
    # do not sure about optimal solution
    best_node, path = simulated_annealing(graph, heuristic, 'A', goal='G')
    
    print("best node: " + best_node)
    print(path)

if __name__ == "__main__":
    main()