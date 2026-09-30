# https://codeforces.com/problemset/problem/1866/B%C3%A2%C2%81%C2%A3
from typing import List
import sys


sys.stdin = open('z.txt','r')

class Solution:
    def __init__(self):
        self.MOD = 998244353

    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(a, a%b)
    
    def lcm(self, a,b):
        return (a / (self.gcd(a,b))) * b
    
    def BattlingNumbers(self, n , nums1, nums2):
        
        return ""


sol = Solution()
t = int(input())
for _ in range(t):
    n = int(input())
    nums1 = map(int, input().split())
    nums2 = map(int, input().split())
    print(sol.BattlingNumbers(n,nums1,nums2))
