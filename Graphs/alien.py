# https://www.geeksforgeeks.org/problems/alien-dictionary/1

from collections import deque

class Solution:
    def findOrder(self, words):
        chars = set()

        for word in words:
            for ch in word:
                chars.add(ch)

        adj = {ch: [] for ch in chars}

        indegree = {ch: 0 for ch in chars}

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            j = 0

            while j < len(word1) and j < len(word2):
                if word1[j] != word2[j]:
                    u = word1[j]
                    v = word2[j]

                    if v not in adj[u]:
                        adj[u].append(v)
                        indegree[v] += 1

                    break

                j += 1
                
            if j == len(word2) and len(word1) > len(word2):
                return ""
                
        q = deque()

        for ch in indegree:
            if indegree[ch] == 0:
                q.append(ch)

        order = []

        while q:
            node = q.popleft()
            order.append(node)

            for neighbor in adj[node]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    q.append(neighbor)
                    
        if len(order) != len(chars):
            return ""

        return "".join(order)