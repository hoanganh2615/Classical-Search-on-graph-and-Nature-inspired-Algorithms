import heapq

def greedy_best_first_search(graph, heuristic, start, goal):
    
    if start == goal:
        return start
    
    # Priority queue entries: (heuristic, node, path)
    frontier = [(heuristic[start], start, [start])]
    visited = set()
    
    while frontier:
        h, current, path = heapq.heappop(frontier)
        
        if current == goal:
            return path
        
        if current in visited:
            continue
        visited.add(current)
        
        for neighbor, weight in graph.get(current, []):
            if neighbor not in visited:
                heapq.heappush(frontier, (heuristic[neighbor], neighbor, path + [neighbor]))
    
    return None

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
    path = greedy_best_first_search(graph, heuristic, 'A', 'G')
    
    print(path)

if __name__ == "__main__":
    main()

    