# https://leetcode.com/problems/subsets-ii/
from typing import List

def subsetsWithDupHelper(nums:List[int], index:int, temp:List[int], ans:List[List[int]]):
        ans.append(temp.copy())
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            temp.append(nums[i])
            subsetsWithDupHelper(nums,i+1,temp,ans)
            temp.pop()

def subsetsWithDup(nums: List[int]):
        nums.sort()
        ans, temp = [],[]
        subsetsWithDupHelper(nums,0,temp,ans)
        return ans

t = int(input())

for _ in range(t):
    nums = list(map(int, input().split()))
    ans = subsetsWithDup(nums)
    print(ans)