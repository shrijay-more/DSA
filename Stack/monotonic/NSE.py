class Solution:
    def nextSmallerElement(self, nums):
        n = len(nums)
        nse = [-1] * n
        st = []

        for i in range(n):
            
            while st and st[-1] >= nums[i]:
                st.pop()

            if st:
                nse[i] = st[-1]

            st.append(nums[i])

        return nse


t = int(input())
sol = Solution()

for _ in range(t):
    nums = list(map(int, input().split()))
    ans = sol.nextSmallerElement(nums)
    print(ans)