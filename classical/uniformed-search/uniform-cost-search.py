import heapq

def uniform_cost_search(graph, start, goal):
    # graph : dict  — { node: [(neighbor, weight), ...] }
    # Returns: list of node labels from start to goal, e.g. ['A', 'B', 'C']
    #          or None if no path exists.

    if start == goal:
        return [start]
    
    # Priority queue entries: (cumulative_cost, node, path)
    frontier = [(0, start, [start])]
    visited = set()
    
    while frontier:
        cost, current, path = heapq.heappop(frontier)
        
        if current == goal:
            return path
        
        if current in visited:
            continue
        visited.add(current)
        
        for neighbor, weight in graph.get(current, []):
            if neighbor not in visited:
                heapq.heappush(frontier, (cost + weight, neighbor, path + [neighbor]))
    
    return None


def main():
    graph = {
    'A': [('B', 2), ('C', 5)],
    'B': [('A', 2), ('C', 1), ('D', 4)],
    'C': [('A', 5), ('B', 1), ('D', 1)],
    'D': [('B', 4), ('C', 1), ('E', 3)],
    'E': [('D', 3)]
    }

    path = uniform_cost_search(graph, 'A', 'E')
    
    print(path)

if __name__ == "__main__":
    main()

    