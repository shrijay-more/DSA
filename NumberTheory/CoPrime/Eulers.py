from typing import List
import sys

sys.stdin  = open('z.txt','r')

class Solution:
    def Eulers_function(self, num:int)->int:
        temp = num
        i = 2
        result = num
        while i*i <= num:
            if temp%i == 0:
                while temp % i == 0:
                    temp = temp//i
                    result = result - result//i
            i+=1

        if temp > 1:
            result = result - (result//temp)

        return result
    
    def EulersOptimal(self, num: int) -> int:
        # Step 1: Initialize phi array
        # phi[i] will eventually store φ(i)
        phi = [0] * (num + 1)
        # Initially assume φ(i) = i
        for i in range(len(phi)):
            phi[i] = i

        # Step 2: Apply sieve logic
        for i in range(2, num + 1):
            
            # If phi[i] == i → i is a prime number
            if phi[i] == i:
                
                # For a prime p: φ(p) = p - 1
                phi[i] = i - 1
                
                # Update all multiples of i
                for multiple in range(2 * i, num + 1, i):
                    # Formula:
                    # φ(n) = φ(n) * (1 - 1/p)
                    # which is same as:
                    # φ(n) = (φ(n) // p) * (p - 1)
                    phi[multiple] = (phi[multiple] // i) * (i - 1)

        # Return φ(num)
        return phi[num]

sol = Solution()
t = int(input())
for _ in range(t):
    num = int(input())
    print(sol.EulersOptimal(num))
