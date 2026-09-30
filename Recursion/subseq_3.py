from typing import List

def subseqsumhelper(nums: List[int], target: int, ans: List[List[int]], arr: List[int], index: int):
    if index == len(nums):
        if target == 0:
            ans.append(arr.copy())
            return True
        return False

    if nums[index] <= target:
        arr.append(nums[index])
        if subseqsumhelper(nums, target - nums[index], ans, arr, index + 1):
            return True
        arr.pop()

    return subseqsumhelper(nums, target, ans , arr, index + 1)


def subseqsum(nums: List[int], target: int):
    ans, arr = [], []
    subseqsumhelper(nums, target, ans, arr, 0)
    return ans


t = int(input())

for _ in range(t):
    nums = list(map(int, input().split()))
    target = int(input())

    ans = subseqsum(nums, target)
    print(ans)