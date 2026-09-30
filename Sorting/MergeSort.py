from typing import List
import sys

sys.stdin = open('z.txt','r')
class Solution:
    def merge(self, nums:List[int], low:int, mid: int, high:int)->None:
        i = low
        j = mid+1
        temp = []
        while i <= mid and j <= high:
            if nums[i] > nums[j]:
                temp.append(nums[j])
                j+=1
            else:
                temp.append(nums[i])
                i+=1
        
        while i<=mid:
            temp.append(nums[i])
            i+=1

        while j<=high:
            temp.append(nums[j])
            j+=1

        for i in range(len(temp)):
            nums[low+i] = temp[i]



    def mergeSort(self, nums:List[int], low:int , high:int)->None:
        if(low>=high):
            return
        mid = low + (high-low)//2
        self.mergeSort(nums,low, mid)
        self.mergeSort(nums,mid+1, high)
        self.merge(nums, low,mid,high)


    def sort(self, nums:List[int])->None:
        low = 0
        high = len(nums)-1
        self.mergeSort(nums, low, high)


s = Solution()
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    s.sort(arr)
    print(arr)
