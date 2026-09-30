# https://leetcode.com/problems/minimum-window-substring/description/
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        dictT = {}
        for c in t:
            dictT[c] = dictT.get(c, 0) + 1

        required = len(dictT)

        l = 0
        formed = 0
        windowCounts = {}

        # (window_length, left, right)
        ans = [float("inf"), 0, 0]

        for r in range(len(s)):
            c = s[r]
            windowCounts[c] = windowCounts.get(c, 0) + 1

            if c in dictT and windowCounts[c] == dictT[c]:
                formed += 1

            while l <= r and formed == required:
                c = s[l]

                if r - l + 1 < ans[0]:
                    ans = [r - l + 1, l, r]

                windowCounts[c] -= 1

                if c in dictT and windowCounts[c] < dictT[c]:
                    formed -= 1

                l += 1

        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]