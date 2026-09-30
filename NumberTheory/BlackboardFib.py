# https://codeforces.com/contest/217/problem/B
from typing import List
import sys
sys.stdin = open('z.txt', 'r')

class Solution:
    def blackboard_fibonacci(self, n: int, r: int) -> None:
        top, bottom = 0, r
        ops = []
        # Step 1: reconstruct operations backwards
        while not (top == 0 and bottom == 1):
            if bottom > top:
                if top == 0:
                    # reduce bottom to 1
                    k = bottom - 1
                    ops.extend(['B'] * k)
                    bottom = 1
                else:
                    k = bottom // top
                    if bottom % top == 0:
                        k -= 1
                    ops.extend(['B'] * k)
                    bottom -= k * top
            else:
                k = top // bottom
                if top % bottom == 0:
                    k -= 1
                ops.extend(['T'] * k)
                top -= k * bottom

        ops.reverse()

        # Step 2: build final sequence of length n
        res = []
        res.append('T')  # first op always T

        idx = 0
        for i in range(1, n):
            if idx < len(ops):
                res.append(ops[idx])
                idx += 1
            else:
                # alternate to minimize mistakes
                if res[-1] == 'T':
                    res.append('B')
                else:
                    res.append('T')

        # Step 3: count mistakes
        mistakes = 0
        for i in range(1, n):
            if res[i] == res[i - 1]:
                mistakes += 1

        print(mistakes)
        print("".join(res))


# driver code
sol = Solution()
t = int(input())
for _ in range(t):
    n1, n2 = map(int, input().split())
    sol.blackboard_fibonacci(n1, n2)