class Solution:
    def prefix_to_postfix(self,s):
        st = [] 
        n = len(s)
        i = n-1
        while i >=0:
            char = s[i]
            if char.isalnum():
                st.append(char)
            else:
                if st:
                    opr1 = st.pop()
                    opr2 = st.pop()
                    expr = opr1 + opr2 + char
                    st.append(expr)
            i-=1

        return  st[-1]

t = int(input())
sol = Solution()
for _ in range(t):
    s = str(input())
    ans =  sol.prefix_to_postfix(s)
    print(ans)
    