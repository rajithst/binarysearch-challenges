class Solution:
    def solve(self, graph):
        visited = {i: 0 for i in range(len(graph))}

        def is_bipartite(node, parent, color):
            visited[node] = color
            for cd in graph[node]:
                if visited[cd] == 0:
                    subr = is_bipartite(cd, node, 3 - color)
                    if not subr:
                        return False

                elif cd != parent and visited[cd] == color:
                    return False
            return True

        result = is_bipartite(0, -1, 1)
        if not result:
            return True

        for i in visited:
            if visited[i] == 0:
                if not is_bipartite(i, -1, 1):
                    return True
        return False
