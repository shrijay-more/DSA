# https://www.geeksforgeeks.org/problems/the-celebrity-problem/1

class Solution:
    def celebrityBrute(self, mat):
        n =  len(mat)
        knowMe = [0] * n
        iKnow = [0] * n
        
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue

                if mat[i][j] == 1:
                    iKnow[i]+=1
                    knowMe[j]+=1
                    
        for i in range(n):
            if iKnow[i] == 0 and knowMe[i] == n-1:
                return i
                
        return -1
    
    def celebrity(self, mat):
        n = len(mat)
        top = 0
        bottom = n-1
        
        while top < bottom:
            if mat[top][bottom] == 1:
                top+=1
            else:
                bottom-=1
                
        for i in range(n):
            if i == top:
                continue
            
            if mat[top][i] == 1:
                return -1
            
            if mat[i][top] ==0:
                return -1
                
        
        return top
            
                
sol = Solution()
t = int(input())

for i in range(t):
    nums = list(map(int, input().split(" ")))
    print(sol.celebrity(nums))