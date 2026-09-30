# https://leetcode.com/problems/asteroid-collision/
from typing import List
class Solution:
    def asteroidCollision(self, nums: List[int]) -> List[int]:
        st = []
        
        for asteroid in nums:
            if asteroid > 0:
                st.append(asteroid)
            else:
                while st and st[-1] > 0 and st[-1] < -asteroid:
                    st.pop()

                if st and st[-1] == -asteroid:
                    st.pop() 

                elif not st or st[-1] < 0:
                    st.append(asteroid)

        return st
    

t = int(input())
sol=  Solution()

t = int(input())

for _ in range(t):
    asteroids = list(map(int, input().split(" ")))
    print(sol.asteroidCollision(asteroids))
