# https://leetcode.com/problems/palindrome-partitioning/
from typing import List

class Solution:
    def isPallindrome(self, s:str):
        i = 0
        j = len(s)-1
        while i < j:
            if s[i] != s[j]:
                return False
            i+=1
            j-=1

        return True

    def partitionHelper(self, s:str, ans:List[List[str]],temp:List[str], index:int):
        if index == len(s):
            ans.append(temp.copy())
            return 
        
        for i in range(index, len(s)):
            if self.isPallindrome(s[index:i+1]):
                temp.append(s[index:i+1])
                self.partitionHelper(s, ans, temp, i+1)
                temp.pop()

    def partition(self, s: str) -> List[List[str]]:
        ans, temp = [],[]
        self.partitionHelper(s, ans, temp,0)
        return ans
    

sol  = Solution()

t = int(input())

for _ in range(t):
    s = str(input())
    ans = sol.partition(s)
    print(ans)