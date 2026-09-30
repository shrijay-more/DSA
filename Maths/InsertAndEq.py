# https://codeforces.com/contest/1902/problem/C%C3%A2%C2%81%C2%A3
import sys
from typing import List

sys.stdin = open('z.txt','r')

class Solution:
    def find_gcd(self, a:int,b:int) ->int:
        if b == 0:
            return a
        return self.find_gcd(b,a%b)
    
    def insert_and_equalize(self, nums:List[int])->None:
        n = len(nums)
        if n == 1:
            print("1")
            return
        nums.sort()
        x = 0 
        for i in range(1,n):
            x = self.find_gcd(x, nums[i]-nums[i-1])

        if x == 0:
            x = 1
        
        maxi = nums[n-1]
        acc_sum = sum(nums)

        res = maxi
        j = n-1
        
        while True:
            while j>=0 and nums[j] > res:
                j-=1

            if j<0 or nums[j] != res:
                break
                
            res-=x
        
        answer = (maxi*(n+1)- (acc_sum+res)) // x
        print(answer)
        

sol = Solution()
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    sol.insert_and_equalize(arr)
