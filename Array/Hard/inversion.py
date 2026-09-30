from typing import List
import sys

sys.stdin = open('z.txt','r')

class Solution:
    def merge(self, nums: List[int], low: int, mid: int, high: int) -> int:
        i = low
        j = mid + 1
        temp = []
        cnt = 0

        while i <= mid and j <= high:
            if nums[i] <= nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                cnt += (mid - i + 1)
                j += 1

        while i <= mid:
            temp.append(nums[i])
            i += 1

        while j <= high:
            temp.append(nums[j])
            j += 1

        # Copy back
        for k in range(len(temp)):
            nums[low + k] = temp[k]

        return cnt


    def mergeSort(self, nums: List[int], low: int, high: int) -> int:
        cnt = 0
        if low >= high:
            return cnt

        mid = low + (high - low) // 2

        cnt += self.mergeSort(nums, low, mid)
        cnt += self.mergeSort(nums, mid + 1, high)
        cnt += self.merge(nums, low, mid, high)

        return cnt


    def sort(self, nums: List[int]) -> int:
        return self.mergeSort(nums, 0, len(nums) - 1)


s = Solution()

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    inv_count = s.sort(arr)
    print(inv_count)