# https://leetcode.com/problems/reverse-words-in-a-string/description/
from typing import List
import sys

sys.stdin = open('z.txt','r')

class Solution:
    def reverseWords(self,s:str)->str:
        s = s.strip()
        words = []
        n = len(s)
        ans = ""
        curr_str = ""
        for i in range(n):
            if s[i] != " ":
                curr_str+=s[i]
            else:
                if curr_str:
                    words.append(curr_str)
                    curr_str=""
        
        words.append(curr_str)

        for i in range(len(words)-1,-1,-1):
            ans+=words[i]
            if i == 0:
                break
            ans+=" "

        return ans
    

    def remove_middle_spaces(self,s:list[str], n:int) -> str:
        i = 0 
        j = 0
        # skip the spaces by shifting them to next index
        while j < n:
            if s[j]!= " " or (j>0 and s[j-1]!= " "):
                s[i] = s[j]
                i+=1
            j+=1

        if i > 0 and s[i-1] == " ":
            i-=1
        return s[:i]
    

    def reverse_words_optimal(self, s:str)-> str:
        s = list(s.strip())
        n = len(s)
        s = self.remove_middle_spaces(s,n)
        s = s[::-1]
        print(s)
        i = 0 
        j = 0
        while j < len(s):
            if s[j] == " ":
                s[i:j] = s[i:j][::-1]
                i = j+1
            j+=1

        s[i:j] = s[i:j][::-1]
        return "".join(s)
    
sol = Solution()
t = int(input())
for _ in range(t):
    s = str(input())
    print(sol.reverse_words_optimal(s))
