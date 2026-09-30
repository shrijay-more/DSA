# iterate from back
# 
class Solution:
    def prefix_to_infix(self,s):
        st = []
        i = len(s)-1

        while i >=0:
            char = s[i]
            if char.isalnum():
                st.append(char)
            else:
                if st:
                    opr1 = st.pop()
                    opr2 = st.pop()
                    expr = '(' + opr1 + char + opr2 + ')'
                    st.append(expr)
            i-=1
        
        return st[-1]
    

t = int(input())
sol = Solution()

for _ in range(t):
    s = str(input())
    ans = sol.prefix_to_infix(s)
    print(ans)

