# https://takeuforward.org/practice/dsa/minimum-multiplications-to-reach-end

from queue import Queue

class Solution:
    def minimumMultiplications(self, arr, start, end):
        MOD = 100000

        dist = [float('inf')] * MOD
        dist[start] = 0

        q = Queue()
        q.put((start, 0))

        while not q.empty():
            node, steps = q.get()

            if node == end:
                return steps

            for num in arr:
                new_node = (node * num) % MOD

                if dist[new_node] > steps + 1:
                    dist[new_node] = steps + 1
                    q.put((new_node, steps + 1))

        return -1