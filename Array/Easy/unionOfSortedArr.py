from typing import List
import sys
sys.stdin = open('z.txt','r')

class Solution:
    def unionSortedArray(self, nums1: List[int], nums2: List[int]) -> list:
        i, j = 0, 0
        ans = []
        n1, n2 = len(nums1), len(nums2)

        while i < n1 and j < n2:
            if nums1[i] == nums2[j]:
                if not ans or ans[-1] != nums1[i]:
                    ans.append(nums1[i])
                i += 1
                j += 1

            elif nums1[i] < nums2[j]:
                if not ans or ans[-1] != nums1[i]:
                    ans.append(nums1[i])
                i += 1

            else:
                if not ans or ans[-1] != nums2[j]:
                    ans.append(nums2[j])
                j += 1

        while i < n1:
            if not ans or ans[-1] != nums1[i]:
                ans.append(nums1[i])
            i += 1

        while j < n2:
            if not ans or ans[-1] != nums2[j]:
                ans.append(nums2[j])
            j += 1

        return ans

s = Solution()
t = int(input())
for _ in range(t):
    n1 = int(input())
    arr1 = list(map(int, input().split()))
    n2 = int(input())
    arr2 = list(map(int, input().split()))
    print(s.unionSortedArray(arr1,arr2))