from typing import List

def subsetsumhelper(nums:List[int],index:int, sum:int, ans:List[int]):
    if index == len(nums):
        ans.append(sum)
        return
    subsetsumhelper(nums, index+1,nums[index]+sum,ans)
    subsetsumhelper(nums,index+1,sum,ans)

def subsetsum(nums:List[int]):
    ans = []
    subsetsumhelper(nums,0,0,ans)
    ans.sort()
    return ans 

t = int(input())

for _ in range(t):
    nums = list(map(int, input().split()))
    ans = subsetsum(nums)
    print(ans)