# https://leetcode.com/problems/permutation-sequence/description/
class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        numbers = []
        fact = 1
        for i in range(1, n):
            fact *= i
            numbers.append(i)
            
        numbers.append(n)
        k = k - 1
        ans = []

        while len(numbers) > 0:
            index = k // fact

            ans.append(str(numbers[index]))
            numbers.pop(index)

            if len(numbers) == 0:
                break

            k = k % fact
            fact = fact // len(numbers)

        return "".join(ans)
    
sol =  Solution()

t = int(input())

for _ in range(t):
    n,k = map(int, input().split())
    ans = sol.getPermutation(n,k)
    print(ans)