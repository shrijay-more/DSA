# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        left = 0
        right = 0
        hashArray= [0]*3
        while right < n:
            hashArray[ord(s[right])-ord('a')]+=1
            while hashArray[0] > 0 and hashArray[1] > 0 and hashArray[2] > 0:
                count+=(n-right)
                hashArray[ord(s[left])- ord('a')]-=1
                left+=1
            
            right+=1

        return count

sol = Solution()

t = int(input())

for _ in range(t):
    s = str(input())
    print(sol.numberOfSubstrings(s))