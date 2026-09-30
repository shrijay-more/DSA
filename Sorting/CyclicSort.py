from typing import List
import sys

sys.stdin =  open('z.txt','r')

class Solution:
    def cyclic_sort(self, nums:List[int]) -> None:
        n = len(nums)
        i = 0
        while i < n :
            correctIndex = nums[i] - 1
            if i < n and nums[i] != nums[correctIndex] and nums[correctIndex] < n:
                nums[i], nums[correctIndex] = nums[correctIndex],nums[i]
            else:
                i+=1

s = Solution()
t =  int(input())

for _ in range(t):
    n =  int(input())
    arr = list(map(int, input().split(" ")))
    s.cyclic_sort(arr)
    print(arr)