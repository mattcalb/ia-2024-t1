"""Implementação da busca em profundidade."""

def dfs (graph, start: int, goal: int):
    if (start in graph and goal in graph):
        anterior = start
        nodesAnalized = 0
        cost = 0
        path = []
        visited = {}
        s = []
        s.append(start)
        while(len(s) > 0):
            v = s.pop()
            visited[v] = False
            if goal == v:
                path.append(v)
                cont = 0
                for node in path:
                    if cont == 0:
                        node_anterior = path[0]
                        cont = cont + 1
                        vertex = path[cont]
                    for i in graph[node_anterior][1:]:
                        if vertex == list(i.keys())[0]:
                            cost = cost + i.get(vertex)
                            cont = cont + 1
                            node_anterior = vertex
                            if(cont < len(path)):
                                vertex = path[cont]
                            break
                return (nodesAnalized, cost, path)
            if visited[v] == False:
                path.append(v)
                visited[v] = True
                for u in graph[v][1:]:
                    s.append(list(u.keys())[0])
    else:
        raise Exception('Vértice não encontrado no grafo')