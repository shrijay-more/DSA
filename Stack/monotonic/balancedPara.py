class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for i in range(len(s)):
            char = s[i]
            if char == '(' or char == '[' or char =='{':
                st.append(char)
            else:
                if not st:
                    return False
                top = st.pop()
                if char == ')' and top != '(':
                    return False
                elif char == ']' and top != '[':
                    return False
                elif char == '}' and top != '{':
                    return False

        return len(st) == 0

