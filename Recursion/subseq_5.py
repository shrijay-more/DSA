from typing import List

def subseqhelper(nums:List[int], sum:int, index:int, temp:List[int]):
    if index == len(nums):
        if sum == 0:
            return 1
        else :
            return 0
        
    left = 0
    if nums[index] <= sum:
        temp.append(nums[index])
        left = subseqhelper(nums, sum - nums[index], index+1,temp)
        temp.pop()

    right = subseqhelper(nums, sum, index+1, temp)

    return left + right

def subseq(nums:List[int], sum:int):
    temp = []
    return subseqhelper(nums, sum, 0, temp)

t = int(input())
for _ in range(t):
    nums = list(map(int, input().split()))
    sum = int(input())
    ans = subseq(nums,sum)
    print(ans)