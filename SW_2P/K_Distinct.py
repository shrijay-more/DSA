# https://www.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1

class Solution:
    def longestKSubstr(self, s, k):
        # code here
        l,r,maxLen = 0,0,-1
        mpp = {}
        n = len(s)

        while r < n:
            if s[r] not in mpp:
                mpp[s[r]] = 1
            elif s[r] in mpp:
                mpp[s[r]]+=1
            
            if len(mpp) > k:
                while len(mpp) >k:
                    mpp[s[l]]-=1
                    if mpp[s[l]] == 0:
                        del mpp[s[l]]

                    l+=1
            
            if len(mpp) ==k:
                maxLen = max(maxLen, r - l +1)
            
            r+=1
        
        return maxLen
        
t = int(input())
sol = Solution()

for _ in range(t):
    nums = list(map(int, input().split(" ")))
    print(sol.longestKSubstr(nums))
    