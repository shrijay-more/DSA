from typing import List
import sys

sys.stdin = open('z.txt','r')

# RADIX : the base of a system of numeration
class Solution:
    def find_length_of_digit(self, digit:int):
        length = 0
        while digit > 0:
            digit = digit//10
            length+=1
        
        return length if length > 0 else 1

    def radix_sort(self, nums:List[int]) -> None:
        n = len(nums)
        maxi = max(nums)
        passes = self.find_length_of_digit(maxi)
        dividend = 1
        for _ in range(passes):
            bucket = [[] for _ in range(10)] 
            for i in range(n):
                num = nums[i]
                num = (num//dividend)%10
                bucket[num].append(nums[i])

            ind = 0
            for j in range(len(bucket)):
                for k in range(len(bucket[j])):
                    nums[ind] = bucket[j][k]
                    ind+=1
            dividend = dividend*10


s = Solution()
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    s.radix_sort(arr)
    print(arr)
