# https://leetcode.com/problems/remove-k-digits/description/
from typing import List

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st = []
        
        for digit in num:
            while st and k > 0 and st[-1] > digit:
                st.pop()
                k -= 1
            st.append(digit)

        while k > 0:
            st.pop()
            k -= 1

        ans = "".join(st).lstrip('0')
        return ans if ans else "0"
    

sol =Solution()
t = int(input())

for i in range(t):
    s = str(input())
    print(sol.removeKdigits(s))

