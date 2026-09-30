# https://leetcode.com/problems/sliding-window-maximum/
from collections import deque
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        ans = []

        for i in range(len(nums)):
            while dq and dq[0] <= i - k:
                dq.popleft()

            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()

            dq.append(i)

            if i >= k - 1:
                ans.append(nums[dq[0]])

        return ans
    

sol = Solution()

t = int(input())

for i in range(t):
    k = int(input())
    nums = list(map(int, input().split(" ")))
    print(sol.maxSlidingWindow(nums,k))