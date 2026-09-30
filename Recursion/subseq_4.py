from typing import List

def subseq_helper(s:str, ans:List[List[str]], temp:str, index:int):
    if index >= len(s):
        ans.append(temp)
        return

    temp+=s[index]
    subseq_helper(s, ans, temp,index+1)
    temp = temp[:-1]
    subseq_helper(s, ans, temp, index+1)


def subseq_string(s:str):
    ans,temp = [],""
    subseq_helper(s, ans, temp,0)
    return ans

t = int(input())
for _ in range(t):
    s = str(input())
    ans = subseq_string(s)
    print(ans)
