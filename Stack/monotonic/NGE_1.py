# https://leetcode.com/problems/next-greater-element-i/description/

class Solution:
    def NGE(self,nums):
        n = len(nums)
        ans = [-1] * n
        st = []
        for i in range(n-1,-1,-1):
            while st and st[-1] <= nums[i]:
                st.pop()
            if st:
                ans[i] = st[-1]
            st.append(nums[i])

        return ans 
    
    def nextGreaterElement(self, nums1, nums2):
        st = []
        n = len(nums2)
        mpp = dict()
        for i in range(n-1,-1,-1):
            while st and st[-1] <= nums2[i]:
                st.pop()

            if st:
                mpp[nums2[i]] = st[-1]
            else:
                mpp[nums2[i]] = -1

            st.append(nums2[i])
        
        for i in range(len(nums1)):
            nums1[i] = mpp.get(nums1[i])

        return nums1


sol = Solution()

t = int(input())

for _ in range(t):
    nums =  list(map(int, input().split()))
    sol.NGE(nums)

                

            