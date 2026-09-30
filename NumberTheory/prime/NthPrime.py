from typing import List
import sys

sys.stdin  = open('z.txt','r')

class Solution:
    def nth_prime(self, n: int) -> int:
        size = 500000
        seive = [1] * size
        seive[0], seive[1] = 0, 0
        for i in range(4, size, 2):
            seive[i] = 0

        i = 3
        while i * i < size:
            if seive[i]:
                for j in range(i * i, size, i):
                    seive[j] = 0
            i += 2

        cnt = 0
        for i in range(2, size):
            if seive[i]:
                cnt += 1
                if cnt == n:
                    return i

        return -1
            
sol = Solution()
t = int(input())
for _ in range(t):
    num = int(input())
    print(sol.nth_prime(num))