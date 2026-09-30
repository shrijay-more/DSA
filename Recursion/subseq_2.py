from typing import List

def subseqsumhelper(nums:List[int], sum:int,arr:List[int], ans:List[List[int]], index:int):
    if index == len(nums):
        if sum == 0:
            ans.append(arr.copy())
        return

    if nums[index] <= sum:
        arr.append(nums[index])
        subseqsumhelper(nums,sum - nums[index], arr,ans, index+1)
        arr.pop()
    
    subseqsumhelper(nums, sum,arr, ans, index+1)


def subseqSum(nums:List[int], sum:int):
    ans, arr = [],[]
    subseqsumhelper(nums,sum, arr,ans,0)
    return ans

t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))
    sum = int(input())
    ans =  subseqSum(arr,sum)
    print(ans)
