# https://leetcode.com/problems/sum-of-subarray-minimums/description/
from typing import List

class Solution:
    def nextSmallerIndex(self, nums:List[int]) -> List[int]:
        n = len(nums)
        nse = [n] * n
        st = []

        for i in range(n-1,-1,-1):
            while st and nums[st[-1]] >= nums[i]:
                st.pop()
            if st:
                nse[i] = st[-1]
            st.append(i)
        return nse

    def previousSmallerIndex(self, nums:List[int]) -> List[int]:
        n = len(nums)
        pse = [-1] * n
        st = []

        for i in range(n):
            while st and nums[st[-1]] > nums[i]:
                st.pop()
            if st:
                pse[i] = st[-1]
            st.append(i)

        return pse
    def sumSubarrayMins(self, nums: List[int]) -> int:
        nse = self.nextSmallerIndex(nums)
        pse = self.previousSmallerIndex(nums)
        ans = 0
        MOD = (10**9) + 7
        n = len(nums)
        for i in range(n):
            left = i - pse[i]
            right = nse[i] - i
            ans = (ans + (nums[i] * left * right)%MOD)%MOD

        return ans
    
sol = Solution()

t = int(input())

for i in range(t):
    nums = list(map(int, input().split(" ")))
    ans = sol.sumSubarrayMins(nums)
    print(ans)