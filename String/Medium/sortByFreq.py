# https://leetcode.com/problems/sort-characters-by-frequency/
from typing import List
import sys

sys.stdin = open('z.txt','r')

class Solution:
    def frequencySort(self, s: str) -> str:
        n =  len(s)
        map = dict()
        ans=""
        arr = [[] for _ in range(n+1)]
        for i in range(n):
            if s[i] in map:
                map[s[i]]+=1
            else:
                map[s[i]]=1
        
        for key,value in map.items():
            arr[value].append(key)

        for i in range(len(arr)-1,-1,-1):
            x = arr[i]
            for j in range(len(x)):
                for k in range(i):
                    ans+=x[j]

        return ans
    
    def frequencySortOptimal(self, s: str) -> str:
        n = len(s)
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        buckets = [[] for _ in range(n + 1)]
        for ch, count in freq.items():
            buckets[count].append(ch)

        ans = []
        for i in range(n, -1, -1):
            for ch in buckets[i]:
                ans.append(ch * i)
        
        return "".join(ans)
    
    
sol = Solution()
t = int(input())
for _ in range(t):
    s = str(input())
    print(sol.frequencySort(s))