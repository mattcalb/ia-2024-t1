"""Implementação da busca em profundidade."""

from queue import deque as Queue

def bfs(graph, start: int, goal: int): #-> (int, float, [int]):
    """Busca um caminho entre start e goal usando busca em largura."""
        
    if(start in graph and goal in graph):
        anterior = start
        nodesAnalized = 0
        cost = 0
        path = []
        visited = {}
        q = Queue()
        q.appendleft(start)
        while (len(q) > 0):
            v = q.pop()
            visited[v] = False
            if(goal == v):
                path.append(v)
                for i in graph[anterior][1:]:
                    if v == list(i.keys())[0]:
                        cost = cost + i.get(v)
                return (nodesAnalized, cost, path)
            if visited[v] == False:
                nodesAnalized = nodesAnalized + 1
                path.append(v)
                for i in graph[anterior][1:]:
                    if v == list(i.keys())[0]:
                        cost = cost + i.get(v)
                anterior = v
                visited[v] = True
                for u in graph[v][1:]:
                    q.appendleft(list(u.keys())[0])

    else:
        raise Exception('Vértice não existente no grafo')