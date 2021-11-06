
class Solution:
    def solve(self, graph):
        visited = {i: 0 for i in range(len(graph))}

        def dfs(node, parent, color):
            visited[node] = color
            for cd in graph[node]:
                if visited[cd] == 0:
                    subr = dfs(cd, node, 3 - color)
                    if not subr:
                        return False

                elif cd != parent and visited[cd] == color:
                    return False
            return True

        result = dfs(0, -1, 1)
        if not result:
            return False

        for i in visited:
            if visited[i] == 0:
                if not dfs(i, -1, 1):
                    return False
        return True
