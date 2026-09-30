import sys

sys.stdin = open('z.txt','r')

class Solution:
    def __init__(self):
        self.MOD = (10**9) + 7

    def modPow(self,base,exponent):
        res = 1 % self.MOD
        while exponent > 0:
            if exponent & 1:
                res = (res * base) % self.MOD
            base = (base * base) % self.MOD
            exponent = exponent >> 1
        return res 
    
    def createStrings(self,s:str):
        n = len(s)
        freq = [0]*26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        # precompute factorials 
        fact = [0] * (n+1)
        fact[0] = 1
        for i in range(1,n+1):
            fact[i] = (fact[i-1]*i) % self.MOD

        denominator = 1
        for i in range(26):
            denominator = (denominator * fact[freq[i]])%self.MOD
        
        numerator = fact[n]
        denominator_inverse = self.modPow(denominator,self.MOD-2)
        ans = (numerator * denominator_inverse) % self.MOD
        return ans

sol = Solution()
t = int(input())
for _ in range(t):
    s =  str(input())
    print(sol.createStrings(s))