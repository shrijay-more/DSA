from typing import List
import sys

sys.stdin= open('z.txt','r')
class Solution:
    def shell_sort(self, nums:List[int])->None:
        n = len(nums)
        gap = n//2
        while gap > 0 :
            for i in range(gap,n):
                temp = nums[i]
                j = i
                while j >= gap and nums[j-gap] > temp:
                    nums[j] = nums[j-gap]\
                    
                    j-=gap

                nums[j] = temp
                
            gap =  gap//2


s= Solution()
t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    s.shell_sort(arr)
    print(arr)
