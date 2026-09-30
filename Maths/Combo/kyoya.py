# https://chatgpt.com/c/69e484ea-9654-8320-badc-0099555e3884
import sys
input = sys.stdin.readline

MOD = 10**9 + 7
MAXN = 2000 + 5

# Precompute factorials and inverse factorials
fact = [1] * MAXN
invFact = [1] * MAXN

def modPow(base, exp):
    res = 1
    while exp:
        if exp & 1:
            res = res * base % MOD
        base = base * base % MOD
        exp >>= 1
    return res

def precompute():
    for i in range(1, MAXN):
        fact[i] = fact[i-1] * i % MOD

    invFact[MAXN-1] = modPow(fact[MAXN-1], MOD-2)
    for i in range(MAXN-1, 0, -1):
        invFact[i-1] = invFact[i] * i % MOD

def nCr(n, r):
    if r < 0 or r > n:
        return 0
    return fact[n] * invFact[r] % MOD * invFact[n-r] % MOD

def solve():
    k = int(input())
    arr = list(map(int, input().split()))

    ans = 1
    s = 0

    for x in arr:
        ans = ans * nCr(s + x - 1, x - 1) % MOD
        s += x

    print(ans)


# Driver
precompute()
t = int(input())
for _ in range(t):
    solve()