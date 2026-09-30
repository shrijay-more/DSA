# https://leetcode.com/problems/3sum/submissions/1962049383/
from typing import List
import sys

sys.stdin = open('z.txt','r')

class Solution:
    def threeSumBrute(self, nums: list[int]) -> list[list[int]]:
        st = set()
        ans = []
        n = len(nums)

        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1,n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        row = [nums[i],nums[j],nums[k]]
                        row.sort()
                        st.add(tuple(row))

        for triplet in st:
            ans.append(list(triplet))
        return ans
    

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        for i in range(n-2):
            if(i > 0 and nums[i] == nums[i-1]):
                continue
            j = i+1
            k = n-1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    ans.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j < k and nums[j] == nums[j-1]:
                        j+=1
                    while j < k and nums[k] == nums[k+1]:
                        k-=1
                elif total < 0:
                    j+=1
                else:
                    k-=1
        return ans
    

s = Solution()

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(s.threeSumBrute(arr))
        