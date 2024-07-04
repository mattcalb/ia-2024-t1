"""Implementação do algoritmo de Dijkstra para o menor caminho em grafos."""

from heapq import heapify, heappush, heappop

def dijkstra(graph, start, goal):
    if start not in graph or goal not in graph:
        raise Exception('Vértice não encontrado no grafo')
    q = []
    dist = {}
    prev = {}
    path = [start]
    visited = 0

    for v in graph:
        dist[v] = float('inf')
        prev[v] = None
        q.append(v)
    
    dist[start] = 0

    while len(q) > 0:
        q.sort(key = lambda x: dist[x])
        u = q.pop(0)
        visited += 1

        if u == goal:
            break

        for v in graph[u][1].keys():
            if v in q:
                alt = dist[u] + graph[u][1][v]
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u

    current_node = goal
    while prev[current_node] != None:
        path.insert(1, current_node)
        current_node = prev[current_node]

    return visited, dist[goal], path