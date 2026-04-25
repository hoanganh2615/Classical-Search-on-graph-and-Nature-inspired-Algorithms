def hill_climbing(graph, start, goal, heuristic):
    
    current = start
    path = [start]
    
    while True:
        neighbors = graph.get(current, [])
        
        if not neighbors:
            break
        
        # Steepest ascent: pick the neighbor with the lowest heuristic value
        best_neighbor = None
        best_h = heuristic.get(current, float('inf'))
        
        for neighbor, _ in neighbors:
            h = heuristic.get(neighbor, float('inf'))
            if h < best_h:
                best_h = h
                best_neighbor = neighbor

        # No improvement — local optimum reached
        if best_neighbor is None:
            break

        current = best_neighbor
        path.append(current)

    return current, path

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
    best_node, path = hill_climbing(graph, 'A', 'G', heuristic)
    
    print("best node: " + best_node)
    print(path)

if __name__ == "__main__":
    main()