class Solution:
    def nextSmallerIndex(self, nums):
        n = len(nums)
        nse = [n] * n
        st = []

        for i in range(n - 1, -1, -1):
            while st and nums[st[-1]] >= nums[i]:
                st.pop()
            if st:
                nse[i] = st[-1]
            st.append(i)

        return nse

    def previousSmallerIndex(self, nums):
        n = len(nums)
        pse = [-1] * n
        st = []

        for i in range(n):
            while st and nums[st[-1]] > nums[i]:
                st.pop()
            if st:
                pse[i] = st[-1]
            st.append(i)

        return pse

    def nextGreaterIndex(self, nums):
        n = len(nums)
        nge = [n] * n
        st = []

        for i in range(n - 1, -1, -1):
            while st and nums[st[-1]] <= nums[i]:
                st.pop()
            if st:
                nge[i] = st[-1]
            st.append(i)

        return nge

    def previousGreaterIndex(self, nums):
        n = len(nums)
        pge = [-1] * n
        st = []

        for i in range(n):
            while st and nums[st[-1]] < nums[i]:
                st.pop()
            if st:
                pge[i] = st[-1]
            st.append(i)

        return pge

    def subArrayRanges(self, nums):
        n = len(nums)

        nse = self.nextSmallerIndex(nums)
        pse = self.previousSmallerIndex(nums)
        nge = self.nextGreaterIndex(nums)
        pge = self.previousGreaterIndex(nums)

        ans = 0

        for i in range(n):
            left_pse = i - pse[i]
            right_nse = nse[i] - i

            left_pge = i - pge[i]
            right_nge = nge[i] - i

            minimum = nums[i] * left_pse * right_nse
            maximum = nums[i] * left_pge * right_nge

            ans += maximum - minimum

        return ans
    
sol = Solution()

t = int(input())

for i in range(t):
    nums = list(map(int, input().split(" ")))
    ans = sol.subArrayRanges(nums)
    print(ans)