# https://codeforces.com/contest/1305/problem/C%C3%A2%C2%81%C2%A3
import sys 
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())

    if n > m:
        print(0)
        return
    
    a = list(map(int, input().split()))

    ans = 1
    for i in range(n):
        for j in range(i + 1, n):
            diff = abs(a[i] - a[j])
            ans = (ans * (diff % m)) % m
    
    print(ans)


t = int(input())
for _ in range(t):
    solve()