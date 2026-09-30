from typing import List
import sys

sys.stdin = open('z.txt','r')

class Solution:
    def count_sort(self, nums: List[int]) -> List[int]:
        n = len(nums)
        maxi = max(nums)
        
        count = [0] * (maxi + 1)

        for num in nums:
            count[num] += 1

        # prefix array to get the correct indices and overall stabitlity of algorithm
        for i in range(1, len(count)):
            count[i] += count[i - 1]
        
        ans = [0] * n

        for i in range(n - 1, -1, -1):
            num = nums[i]
            ans[count[num] - 1] = num
            count[num] -= 1

        return ans


s = Solution()
t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(s.count_sort(arr))