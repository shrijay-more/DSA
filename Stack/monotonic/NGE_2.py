# https://leetcode.com/problems/next-greater-element-ii/
from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nge = [-1] * n
        for i in range(n):
            for j in range(i+1, n+i):
                ind = j % n
                if nums[ind] > nums[i]:
                    nge[i] = nums[ind]
                    break
        return nge

    def nextGreaterElementsOptimized(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nge = [-1] * n
        st = []
        for i in range(2*n-1,-1,-1):
            i = i % n
            while st and st[-1] <= nums[i]:
                st.pop()
            
            if st:
                nge[i] = st[-1]
            
            st.append(nums[i])

        return nge

t = int(input())
sol = Solution()

for _ in range(t):
    nums= list(map(int, input().split()))
    ans = sol.nextGreaterElements(nums)
    print(ans)

