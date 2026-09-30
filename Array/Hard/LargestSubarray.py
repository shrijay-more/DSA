# https://www.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1
class Solution:
    def maxLength(self, nums):
        k =0
        n = len(nums)
        map = dict()
        prefixSum,maxLen = 0,0
        for i in range(n):
            prefixSum+=nums[i]
            
            if prefixSum == 0:
                maxLen = i+1
                
            if prefixSum-k in map:
                maxLen = max(maxLen, i - map[prefixSum-k])
            
            if prefixSum-k not in map:
                map[prefixSum-k] = i
                
        return maxLen
        
s = Solution()
t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(s.maxLength(arr))