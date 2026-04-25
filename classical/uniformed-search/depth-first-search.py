def depth_first_search(graph, start, goal):
    # graph : dict  — { node: [(neighbor, weight), ...] }
    # Returns: list of node labels from start to goal, e.g. ['A', 'B', 'C']
    #          or None if no path exists.
    
    if start == goal:
        return [start]
    
    # Use stack to stores (current_node, path_so_far)
    frontier = [(start, [start])]
    
    visited = set()
    visited.add(start)
    
    while frontier:
        current, path = frontier.pop() # LIFO - process deepest node first 
        
        for neighbor, weight in graph[current]:
            if neighbor == goal:
                return path + [neighbor] # Found the goal!
            
            if neighbor not in visited:
                visited.add(neighbor)
                frontier.append((neighbor, path + [neighbor]))
    
    return None # No path found



def main():
#     test 1
#     graph = {
#     'A': [('B', 3), ('C', 4), ('D', 5)],
#     'B': [('A', 3), ('C', 4), ('E', 5)],
#     'C': [('A', 4), ('B', 4)],
#     'D': [('A', 5)],
#     'E': [('B', 5), ('F', 10), ('G', 12)],
#     'F': [('E', 10)],
#     'G': [('E', 12)]
# } 
    graph = {
    'A': [('B', 2), ('C', 5)],
    'B': [('A', 2), ('C', 1), ('D', 4)],
    'C': [('A', 5), ('B', 1), ('D', 1)],
    'D': [('B', 4), ('C', 1), ('E', 3)],
    'E': [('D', 3)]
    }

    path = depth_first_search(graph, 'A', 'E')
    
    print(path)

if __name__ == "__main__":
    main()