# https://leetcode.com/problems/permutations/
from typing import List
def permuteHelper1(nums: List[int], ans: List[List[int]],
                      temp: List[int], vis: List[bool], index: int):

        if index == len(nums):
            ans.append(temp.copy())
            return

        for i in range(len(nums)):

            if not vis[i]:

                temp.append(nums[i])
                vis[i] = True

                permuteHelper1(nums, ans, temp, vis, index + 1)

                vis[i] = False
                temp.pop()

def permuteHelper2(nums: List[int], ans: List[List[int]],index: int):
    if index == len(nums):
        ans.append(nums.copy())
        return
    
    for i in range(index,len(nums)):
        nums[index],nums[i] = nums[i], nums[index]
        permuteHelper2(nums,ans,index+1)
        nums[index],nums[i] = nums[i],nums[index]
        
def permute(nums: List[int]) -> List[List[int]]:

    ans = []
    temp = []
    vis = [False] * len(nums)
    permuteHelper1(nums, ans, temp, vis, 0)
    return ans

t = int(input())

for _ in range(t):
    nums = list(map(int, input().split()))
    ans = permute(nums)
    print(ans)