class Solution:
    def postfix_to_prefix(self, s):
        st = []
        i = 0 
        n =  len(s)

        while i  < n :
            char =  s[i]
            if char.isalnum():
                st.append(char)
            else:
                if st:
                    opr1 =  st.pop()
                    opr2 =  st.pop()
                    expr = char + opr2 + opr1
                    st.append(expr)

            i+=1

        return st[-1]


t =  int(input())
sol = Solution()

for _ in range(t):
    s =  str(input())
    ans  = sol.postfix_to_prefix(s)
    print(ans)