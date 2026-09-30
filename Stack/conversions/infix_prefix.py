# Reverse the infix expression
# Infix to postfix
# Reverse that answer
class Solution:
    def precedence(self,char):
        if char == "+" or char =="-":
            return 1
        elif char == "*" or char == "/":
            return 2
        elif char == "^":
            return 3
        else:
            return 0
        
    def infix_to_prefix(self,s):
        s = s[::-1]
        s = list(s)
        for i in range(len(s)):
            if s[i] == '(':
                s[i] = ')'

            elif s[i] == ')':
                s[i] = '('

        st = []
        ans = ""
        n = len(s)
        i = 0 
        while i < n:
            char = s[i]
            if char >= 'A' and char <= 'Z' or char >= 'a' and char <= 'z' and char >='0' and char <='9':
                ans+=char
            
            elif char == '(':
                st.append(char)
            elif  char == ')':
                while st and st[-1] != '(':
                    ans+=st.pop()
                st.pop()
            else:
                if char == '^':
                    while st and self.precedence(char) <= self.precedence(st[-1]):
                        ans += st.pop()
                else:
                    while st and self.precedence(char) < self.precedence(st[-1]):
                        ans += st.pop()
                st.append(char)
            i+=1
            

        while st:
            ans += st.pop()

        ans = ans[::-1]
        return ans

t = int(input())
sol = Solution()

for _ in range(t):
    s = str(input())
    ans = sol.infix_to_prefix(s)
    print(ans)

