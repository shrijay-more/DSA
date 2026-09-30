# https://leetcode.com/problems/two-sum/
from typing import List
import sys
sys.stdin = open('z.txt','r')

class Solution:
    def twoSum(self, nums:List[int], target:int)->int : 
        map = dict()

        for i in range(len(nums)):
            needed = target - nums[i]

            if needed in map:
                return [map[needed],i]
            else:
                map[nums[i]]=i

        return [-1,-1]



s = Solution()
t = int(input())

for _ in range(t):
    n = int(input())
    target = int(input())
    arr = list(map(int, input().split()))
    print(s.twoSum(arr, target))