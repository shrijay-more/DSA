# https://www.codechef.com/problems/RIFFLES
from typing import List
import sys

sys.stdin = open('z.txt','r')

class Solution:
    def chef_and_riffles(self, N: int, K: int) -> List[int]:
        half = N // 2

        # base permutation (one riffle)
        base = [0] * (N + 1)
        for i in range(1, N + 1):
            if i <= half:
                base[i] = 2 * i - 1
            else:
                base[i] = 2 * (i - half)

        # identity permutation
        res = list(range(N + 1))

        # permutation composition
        def compose(A, B):
            C = [0] * (N + 1)
            for i in range(1, N + 1):
                C[i] = A[B[i]]
            return C

        # binary exponentiation on permutation
        while K > 0:
            if K & 1:
                res = compose(res, base)
            base = compose(base, base)
            K >>= 1

        return res[1:]   # ignore index 0


sol = Solution()
t = int(input())

for _ in range(t):
    N, K = map(int, input().split())
    ans = sol.chef_and_riffles(N, K)
    print(*ans)