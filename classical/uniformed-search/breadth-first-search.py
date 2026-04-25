from collections import deque

def reconstruct_path(parent, start, goal):
    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()
    return path

def breath_first_search(graph, start, goal):
    # graph : dict  — { node: [(neighbor, weight), ...] }
    # Returns: list of node labels from start to goal, e.g. ['A', 'B', 'C']
    #          or None if no path exists.
    if start == goal:
        return [start]
    
    # Queue for BFS
    frontier = deque()
    frontier.append(start)
    
     # Store parent of each visited node
    parent = {start: None}
    
    while frontier:
        current = frontier.popleft()  # FIFO
        
        for neighbor, weight in graph[current]:
            if neighbor not in parent:
                parent[neighbor] = current
            
                if neighbor == goal:
                    return reconstruct_path(parent, start, goal)

                frontier.append(neighbor)
    
    return None # No path found
# psedocode
# BreathFirstSearch(graph, the weitghted graph,
#                   start, the start node that inital with 'A',
#                   goal, the goal node that inital with 'G')
#
#   frontier = [start]
#   parent = {start: None}
#   while not frontier is empty
#       node = pop(frontier) # FIFO queue
#       if the node is the goal then
#           return solution
#       for child in graph[node]:
#           s = child.state
#           if s is the goal:
#               return solution
#           if s is not in reached:
#               add(frontier, child)
#               add(reached, s)
#   return false         

def main():
    graph = {
    'A': [('B', 2), ('C', 5)],
    'B': [('A', 2), ('C', 1), ('D', 4)],
    'C': [('A', 5), ('B', 1), ('D', 1)],
    'D': [('B', 4), ('C', 1), ('E', 3)],
    'E': [('D', 3)]
    }

    path = breath_first_search(graph, 'A', 'E')
    
    print(path)

if __name__ == "__main__":
    main()

    