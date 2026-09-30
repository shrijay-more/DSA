from typing import List
import sys

sys.stdin = open('z.txt','r')

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        cnt1,cnt2 = 0,0,
        ele1,ele2 = float('-inf'),float('-inf')

        for i in range(n):
            if cnt1 == 0 and ele2 != nums[i]:
                cnt1=1
                ele1 = nums[i]
            
            elif cnt2 == 0 and ele1 != nums[i]:
                cnt2 = 1
                ele2= nums[i]
            
            elif ele1 == nums[i]:
                cnt1+=1
            elif ele2 == nums[i]:
                cnt2+=1
            else: 
                cnt1-=1
                cnt2-=1
        
        cnt1,cnt2=0,0

        for i in range(n):
            if ele1 == nums[i]:
                cnt1+=1
            if ele2 == nums[i]:
                cnt2+=1

        mini = int((n//3)+1)

        if cnt1 >= mini:
            ans.append(ele1)
        if cnt2 >= mini:
            ans.append(ele2)
        return ans


s= Solution()
t = int(input())

for _ in range(t):
    n = int(input())
    arr= list(map(int ,input().split()))
    print(s.majorityElement(arr))