"""Implementação do algoritmo de Dijkstra para o menor caminho em grafos."""
from heapq import heapify, heappush, heappop

def dijkstra(graph, start, goal):
    if start not in graph or goal not in graph:
        raise Exception('Vértice não encontrado no grafo')
    return
