class Solution:
    def precedence(self, char):
        if char == '^':
            return 3
        elif char == '+' or char == '-':
            return 1
        elif char == '*' or char =='/':
            return 2
        else:
            return 0
        
    def infix_to_postfix(self,s):
        ans = ""
        st = []
        n = len(s)
        i = 0 
        while i < n:
            char = s[i]
            if char >= 'A' and char <= 'Z' or char >= 'a' and char <'z' or char >= '0' and  char <= '9':
                ans+=char

            elif char == '(':
                st.append(char)

            elif char == ')':
                while len(st) != 0 and st[len(st)-1] != '(':
                    ans+=st.pop()

                st.pop()

            else:
                while len(st) != 0 and self.precedence(char) <= self.precedence(st[len(st)-1]):
                    opr = st.pop()
                    ans+=opr
                
                st.append(char)

            i+=1


        while len(st) != 0:
            ans+=st.pop()

        return ans 


    
        
sol = Solution()

t = int(input())

for _ in range(t):
    s = str(input())
    ans = sol.infix_to_postfix(s)
    print(ans)

    
            
