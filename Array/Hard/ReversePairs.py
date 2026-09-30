# https://leetcode.com/problems/reverse-pairs/description/
from typing import List
import sys

sys.stdin = open('z.txt','r')
class Solution:
    def merge(self, nums: List[int], low: int, mid: int, high: int) -> None:
        i = low
        j = mid + 1
        temp = []

        while i <= mid and j <= high:
            if nums[i] <= nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                j += 1

        while i <= mid:
            temp.append(nums[i])
            i += 1

        while j <= high:
            temp.append(nums[j])
            j += 1

        for k in range(len(temp)):
            nums[low + k] = temp[k]

    def countRevPairs(self, nums: List[int], low: int, mid: int, high: int) -> int:
        cnt = 0
        j = mid + 1

        for i in range(low, mid + 1):
            while j <= high and nums[i] > 2 * nums[j]:
                j += 1
            cnt += (j - (mid + 1))

        return cnt

    def mergeSort(self, nums: List[int], low: int, high: int) -> int:
        if low >= high:
            return 0

        mid = (low + high) // 2
        cnt = 0

        cnt += self.mergeSort(nums, low, mid)
        cnt += self.mergeSort(nums, mid + 1, high)
        cnt += self.countRevPairs(nums, low, mid, high)
        self.merge(nums, low, mid, high)

        return cnt

    def reversePairs(self, nums: List[int]) -> int:
        return self.mergeSort(nums, 0, len(nums) - 1)


s = Solution()
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(s.reversePairs(arr))