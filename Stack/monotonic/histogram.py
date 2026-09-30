# https://leetcode.com/problems/largest-rectangle-in-histogram/
from typing import List
class Solution:
    def largestRectangleAreaBrute(self, heights: List[int]) -> int:
        n = len(heights)
        ans = 0 
        for i in range(n):
            j = i-1
            k = i+1
            width = 1
            while j>=0 and heights[j] >= heights[i]:
                width+=1
                j-=1

            while k < n and heights[k] >= heights[i]:
                width+=1
                k+=1

            ans = max(ans, (heights[i]*width))

        return ans
    

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
    
sol = Solution()
t = int(input())

for i in range(t):
    heights = list(map(int, input().split(" ")))
    ans = sol.largestRectangleAreaBrute(heights)
    print(ans)