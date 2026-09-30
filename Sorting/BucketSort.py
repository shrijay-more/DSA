from typing import List
import sys

sys.stdin = open('z.txt','r')

class Solution:
    def BucketSort(self, nums:List[float]) -> None:
        n = len(nums)
        bucket = [[] for _ in range(n)]

        for i in range(n):
            ele = int(nums[i]*n)
            if ele == n:
                ele = n - 1
            bucket[ele].append(nums[i])

        for i in range(len(bucket)):
            bucket[i].sort()

        index = 0
        for i in range(len(bucket)):
            
            for j in range(len(bucket[i])):
                nums[index] = bucket[i][j]
                index+=1

    def bucket_sort1(self, nums: List[float]) -> None:
        n = len(nums)
        
        if n <= 1:
            return
        
        min_val = min(nums)
        max_val = max(nums)

        if min_val == max_val:
            return
        buckets = [[] for _ in range(n)]

        for num in nums:
            index = int((num - min_val) / (max_val - min_val) * (n - 1))
            buckets[index].append(num)

        for bucket in buckets:
            bucket.sort()
        idx = 0
        for bucket in buckets:
            for num in bucket:
                nums[idx] = num
                idx += 1
                
s =  Solution()
t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(float, input().split()))
    s.BucketSort(arr)
    print(arr)


