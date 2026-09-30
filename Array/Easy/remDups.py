# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
from typing import List
import sys 
sys.stdin = open('z.txt','r')

class Solution:
    def removeDuplicates(this,nums:  List[int])->int:
        i,j =  0,0
        n = len(nums)

        while j < n :
            if nums[i] == nums[j]:
                j = j+1
            else:
                temp = nums[j]
                nums[j] = nums[i+1]
                nums[i+1]= temp
                i=i+1
                j=j+1
        
        return i + 1
    

s = Solution()

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(s.removeDuplicates(arr))
    print(arr)