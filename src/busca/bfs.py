"""Implementação da busca em profundidade."""

from collections import deque

def bfs(graph, start, goal):
    """Busca um caminho entre start e goal usando busca em largura."""

    if start not in graph or goal not in graph:
        raise Exception('Vértice não encontrado no grafo')
    
    # Inicialização das variáveis
    queue = deque([start])
    visited = {start: True}
    predecessor = {start: None}
    costs = {start: 0}
    nodesAnalized = 0
    path = []

    while queue:
        current_node = queue.popleft()
        nodesAnalized = nodesAnalized + 1

        if current_node == goal:
            total_cost = costs[current_node]
            while current_node is not None:
                path.append(current_node)
                current_node = predecessor[current_node]
            path.reverse()
            return (nodesAnalized, total_cost, path)

        # Verificar todos os vizinhos do nó atual
        for neighbor in graph[current_node][1:]:
            neighbor_node, neighbor_cost = list(neighbor.items())[0]
            if neighbor_node not in visited:
                visited[neighbor_node] = True
                predecessor[neighbor_node] = current_node
                costs[neighbor_node] = costs[current_node] + neighbor_cost
                queue.append(neighbor_node)