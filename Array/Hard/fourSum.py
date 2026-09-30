# https://leetcode.com/problems/4sum/description/
from typing import List
import sys

sys.stdin =  open('z.txt','r')

class Solution:
    def fourSumBrute(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        ans = []
        st = set()
        for i in range(n-3):
            for j in range(i+1,n-2):
                for k in range(j+1,n-1):
                    for l in range(k+1,n):
                        total = nums[i] + nums[j] + nums[k] + nums[l]
                        if total == target:
                            row =  [nums[i],nums[j],nums[k],nums[l]]
                            row.sort()
                            st.add(tuple(row))
        for x in st:
            ans.append(list(x))

        return ans
    
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,n):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                k = j+1
                l = n-1
                while k < l:
                    total = nums[i] + nums[j] + nums[k] + nums[l]
                    if total == target:
                        ans.append([nums[i], nums[j], nums[k], nums[l]])
                        k+=1
                        l-=1
                        while k<l and nums[k] == nums[k-1]:
                            k+=1
                        while k<l and nums[l] == nums[l+1]:
                            l-=1
                    elif total < target:
                        k+=1
                    else:
                        l-=1

        return ans

s= Solution()
t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(s.fourSum(arr))
