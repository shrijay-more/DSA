from typing import List

def subSequenceHelper(nums:List[int],arr:List[int] , ans:List[List[int]], index:int, length:int):
    if (index >= length):
        ans.append(arr.copy())
        return

    arr.append(nums[index])
    subSequenceHelper(nums, arr, ans, index+1, length)
    arr.pop()
    subSequenceHelper(nums, arr, ans, index+1, length)


def subSequence(nums:List[int]):
    ans,arr = [],[]
    subSequenceHelper(nums, arr,ans,0,len(nums))
    return ans

t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))
    ans = subSequence(arr)
    print(ans)
    