# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstringBrute(self, s: str) -> int:
        n = len(s)
        mpp = {}
        l,r,maxLen = 0,0,0

        while l < n and r < n:
            if s[r] not in mpp:
                mpp[s[r]] = 1
                maxLen = max(maxLen, r-l+1)
                r+=1
            elif s[r] in mpp:
                del mpp[s[l]]
                l+=1

        return maxLen

    def lengthOfLongestSubstringOptimal(self, s: str) -> int:
        n = len(s)
        hash = [-1] * 256

        l,r, maxLen = 0,0,0

        while r < n :
            idx = ord(s[r])

            if hash[idx] is not -1:
                l = max(hash[idx]+1,l)
            
            maxLen = max(maxLen,r-l+1)

            hash[idx] = r
            r+=1

        return maxLen

sol = Solution()

t = int(input())

for _ in range(t):
    s =  str(input())
    print(sol.lengthOfLongestSubstringOptimal(s))

                

                

