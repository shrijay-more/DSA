from typing import List
import sys

sys.stdin  = open('z.txt','r')

class Solution:
    def commonDivisors(self, nums:List[int])->int:
        maxi = max(nums)
        freq = [0] *(maxi+1)
        for x in nums:
            freq[x]+=1

        for i in range(maxi, 1,-1):
            count = 0
            for j in range(i,maxi+1,i):
                count+=freq[j]
                if count >=2:
                    return i
                
        return 1

sol = Solution()
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(sol.commonDivisors(arr))
