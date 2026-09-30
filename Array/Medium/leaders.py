from typing import List
import sys

sys.stdin = open('z.txt','r')

class Solution:
    def leader(self, nums:List[int])->List[int]:
        n = len(nums)
        ans = []
        ans.append(nums[n-1])
        maxi = nums[n-1]
        for i in range(n-2,-1,-1):
            if nums[i] > maxi:
                ans.append(nums[i])
                maxi = nums[i]

        ans[:] = ans[::-1]
        return ans

s = Solution()
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(s.leader(arr))