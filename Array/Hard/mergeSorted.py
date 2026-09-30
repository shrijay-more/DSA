# https://leetcode.com/problems/merge-sorted-array/description/
from typing import List
import sys
sys.stdin = open('z.txt','r')

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        last = m+n-1

        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m-1]
                m-=1
            else:
                nums1[last] = nums2[n-1]
                n-=1
            last-=1

        while n > 0:
            nums1[last] = nums2[n-1]
            n,last =  n-1, last-1
    
            
s =  Solution()
t = int(input())

for _ in range(t):
    n1,n2 = map(int, input().split())
    nums1 = list(map(int, input().split()))
    nums2 = list(map(int, input().split()))
    s.merge(nums1,len(nums1)-len(nums2), nums2, n2)
    print(nums1)