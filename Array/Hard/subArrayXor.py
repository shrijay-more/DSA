# https://www.geeksforgeeks.org/problems/count-subarray-with-given-xor/1

from typing import List
import sys

sys.stdin = open('z.txt','r')

class Solution:
    def subArrayXor(self, nums:List[int], k:int)-> int :
        map = dict()
        n = len(nums)
        map[0] =1
        cnt = 0 
        prefixXor = 0
        for i in range(len(nums)):
            prefixXor^=nums[i]
            
            if prefixXor^k in map:
                cnt+=map[prefixXor^k]
            
            if prefixXor in map:
                map[prefixXor]+=1
                
            else:
                map[prefixXor] = 1
                
        return cnt


s = Solution()
t =int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(s.subArrayXor(arr))

