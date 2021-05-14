# -*- coding: utf-8 -*-
"""
Created on Wed May  5 18:26:16 2021

@author: Christian
"""
from sys import maxsize

def get_distances(graph, initial):
    """"
    An implementation of the Bellman Ford algorithm to calculate the minimal
    distance from an initial node.
    
    :param graph: The graph represented as a dictionary. For example:
        
        graph = {
            's' : {'t':6, 'y':7},
            't' : {'x':5, 'z':-4, 'y':8 },
            'y' : {'z':9, 'x':-3},
            'z' : {'x':7, 's': 2},
            'x' : {'t':-2}
            }
    
    :param initial: A key denoting the initial node from which to calculate
    the distances. For example: initial = 's' (for the previous graph example)
    
    :return: A dictionary mapping each vertix to its minimum distance.
    """
    # Initialize the distance dictionary
    d = {v: maxsize for v in graph.keys()}
    d[initial] = 0
    
    # Iterate n - 1 times where n is the size of number of vertices on the graph
    for _ in range(len(graph) - 1):
        
        # For each pair (u, v) update the minimum distance
        for u, adjacent_vertices in graph.items():
            for v, weight in adjacent_vertices.items():
                d[v] = min(d[v], d[u] + weight)
                
    return d

graph = {
    's' : {'t':6, 'y':7},
    't' : {'x':5, 'z':-4, 'y':8 },
    'y' : {'z':9, 'x':-3},
    'z' : {'x':7, 's': 2},
    'x' : {'t':-2}
}
print(get_distances(graph,'s'))