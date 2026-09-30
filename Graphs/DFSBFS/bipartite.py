# https://leetcode.com/problems/is-graph-bipartite/
from queue import Queue
from typing import List

class BFS:
    def bfs(self, start, graph, color):
        q = Queue()
        q.put(start)
        color[start] = 0

        while not q.empty():
            node = q.get()
            for neighbor in graph[node]:
                if color[neighbor] == -1:
                    color[neighbor] = 1 - color[node]
                    q.put(neighbor)
                elif color[neighbor] == color[node]:
                    return False

        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n

        for i in range(n):
            if color[i] == -1:
                if not self.bfs(i, graph, color):
                    return False

        return True


class DFS:
    def dfs(self, graph, color, node, col):
        color[node] = col

        for neighbor in graph[node]:
            if color[neighbor] == -1:
                if not self.dfs(graph, color, neighbor, 1 - col):
                    return False
            elif color[neighbor] == col:
                return False

        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        v = len(graph)
        color = [-1] * v

        for i in range(v):
            if color[i] == -1:
                if not self.dfs(graph, color, i, 0):
                    return False

        return True