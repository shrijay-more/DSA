# https://leetcode.com/problems/next-permutation/description/
from typing import List 
import sys

sys.stdin = open('z.txt','r')

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        partitionInd = -1

        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                partitionInd = i
                break

        if partitionInd == -1:
            nums[:] = nums[::-1]
            return

        for i in range(n-1, partitionInd, -1):
            if nums[i] > nums[partitionInd]:
                smallestAfterPartitionInd = i
                break

        nums[partitionInd], nums[smallestAfterPartitionInd] = nums[smallestAfterPartitionInd], nums[partitionInd]

        nums[partitionInd+1:] = reversed(nums[partitionInd+1:])


s = Solution()
t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    s.nextPermutation(arr)
    print(arr)