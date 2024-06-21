def dfs(graph, start, goal):
    if start not in graph or goal not in graph:
        raise Exception('Vértice não encontrado no grafo')

    stack = [(start, [start], 0)]
    visited = set()
    nodesAnalized = 0

    while stack:
        (v, path, cost) = stack.pop()
        nodesAnalized += 1

        if v == goal:
            return nodesAnalized, cost, path

        if v not in visited:
            visited.add(v)
            for edge in graph[v][1:]:
                neighbor = list(edge.keys())[0]
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    new_cost = cost + edge[neighbor]
                    stack.append((neighbor, new_path, new_cost))