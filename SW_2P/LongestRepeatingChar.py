# https://leetcode.com/problems/longest-repeating-character-replacement/description/
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0] * 26
        maxLen, maxFreq = 0, 0
        l = 0

        for r in range(len(s)):
            freq[ord(s[r]) - ord('A')] += 1
            maxFreq = max(maxFreq, freq[ord(s[r]) - ord('A')])

            while (r - l + 1) - maxFreq > k:
                freq[ord(s[l]) - ord('A')] -= 1
                l += 1
                
                maxFreq = 0
                for i in range(26):
                    maxFreq = max(maxFreq, freq[i])

            maxLen = max(maxLen, r - l + 1)

        return maxLen
    
sol  =Solution()

t = int(input())

for _ in range(t):
    s = str(input())
    k = int(input())
    print(sol.characterReplacement(s,k))