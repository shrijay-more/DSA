# https://leetcode.com/problems/combination-sum-ii/description/
from typing import List

def combinationSum2Helper(candidates:List[int], target:int, ans:List[List[int]], temp:List[int], index:int):
        if target == 0:
            ans.append(temp.copy())
            return
        
        if index == len(candidates) or target < 0 :
            return 

        if candidates[index] <= target:
            for i in range(index,len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                temp.append(candidates[i])
                combinationSum2Helper(candidates, target - candidates[i], ans, temp, i+1)
                temp.pop()

def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
        ans, temp = [],[]
        candidates.sort()
        combinationSum2Helper(candidates, target,ans, temp, 0)
        return ans

t = int(input())
for _ in range(t):
    nums = list(map(int, input().split()))
    target = int(input())
