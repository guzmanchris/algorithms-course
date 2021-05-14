from sys import maxsize # Import the maximum value for an int.
import heapq as q
from collections import defaultdict

def create_spanning_tree(graph, initial):
    # Use the maximum size as a representation of infinity   
    inf = maxsize  
    
    # Create key dict. All values not found return inf.
    key = defaultdict(lambda: inf)
    key[initial] = 0
    
    # Create path dict. All values not found return None.
    path = defaultdict(lambda: None)
    
    # Create and fill priority queueu
    Q = [ (key[v], v) for v in graph.keys() ]
    q.heapify(Q)
    
    # Create an empty dict to store the MST
    A = dict()
    
    # While there are unexplored vertices keep expanding.
    while Q:
        # Retrieve element with min cost.
        u = q.heappop(Q)[1]
        # Add to path.
        if u != initial:
            A[ path[u] ] = {u}
        # Verify and update cost of successors.
        for v, cost in graph[u].items():
            
            # Check if v is in Q and store its position.
            try:
                i = Q.index((key[v], v))
                found = True
            except ValueError:
                found = False
            
            # Update key, path, and Q if necessary
            if found and cost < key[v]:
                key[v] = cost
                
                # Update the cost to reach v in Q. heapq does not include a
                # decrease_key function. To impliment this functionality
                # we simply treat Q as a list and replace the value. Then
                # run heapify(Q) to restore its heap property. This is done in
                # O(n). This can be solved more efficiently with _siftdown and
                # _siftup methods from heapq but, the methods are considered to
                # be for internal use and, are therefore not considered in this
                # implementation. For now O(n) complexity is accepted.
                Q[i] = (key[v], v)
                q.heapify(Q)
                
                path[v] = u
    
    return A
    
example_graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 12, 'D': 10, 'E': 4},
    'C': {'A': 3, 'B': 12, 'F': 5},
    'D': {'B': 10, 'E': 7},
    'E': {'B': 4, 'D': 7, 'F': 16},
    'F': {'C': 5, 'E': 16, 'G': 9},
    'G': {'F': 9},
}
print(dict(create_spanning_tree(example_graph, 'D')))
