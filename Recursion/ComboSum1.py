# https://leetcode.com/problems/combination-sum/
from typing import List

def combinationSumHelper(candidates:List[int], target:int, ans:List[List[int]], temp:List[int], index:int):
        if target == 0:
            ans.append(temp.copy())
            return
        if target < 0 or index == len(candidates):
            return
            
        if candidates[index] <= target:
            temp.append(candidates[index])
            combinationSumHelper(candidates, target-candidates[index], ans, temp, index)
            temp.pop()
            combinationSumHelper(candidates, target, ans, temp, index+1)

def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
        ans, temp = [],[]
        combinationSumHelper(candidates, target, ans , temp, 0)
        return ans


t = int(input())
for _ in range(t):
      nums = list(map(int, input().split()))
      target = int(input())
      ans = combinationSum(nums, target)
      print(ans)
