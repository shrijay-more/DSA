# https://leetcode.com/problems/maximal-rectangle/
from typing import List

class Solution:
    def previousSmallerIndex(self,nums:List[int], n:int)->List[int]:
        psi = [-1] * n
        st=[]
        for i in range(n):
            while st and nums[st[-1]] > nums[i]:
                st.pop()
            if st:
                psi[i] = st[-1]

            st.append(i)
        
        return psi

    def nextSmallerIndex(self,nums:List[int], n:int) -> List[int]:
        nsi = [n] * n
        st=[]
        for i in range(n-1, -1,-1):
            while st and nums[st[-1]] >= nums[i]:
                st.pop()

            if st:
                nsi[i] = st[-1]
            
            st.append(i)

        return nsi

            
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        ans = 0 
        psi = self.previousSmallerIndex(heights,n)
        nsi = self.nextSmallerIndex(heights,n)
        for i in range(n):
           ans = max(ans, heights[i] * ((nsi[i] - psi[i]) - 1))
           
        return ans
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        ans = 0
        nums = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    nums[j] += 1
                else:
                    nums[j] = 0

            ans = max(ans, self.largestRectangleArea(nums))

        
        return ans

        
sol = Solution()

t = int(input())

for i in range(t):
    matrix = []
    rows = int(input())
    for i in range(rows):
        arr = list(map(str, input().split(" ")))
        matrix.append(arr)

    print(sol.largestRectangleArea(matrix))