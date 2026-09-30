import sys
sys.stdin = open('z.txt', 'r')

def second_largest(arr):
    largest = float('-inf')
    second_largest = float('-inf')

    for x in arr:
        if x > largest:
            second_largest = largest
            largest = x
        elif x < largest and x > second_largest:
            second_largest = x

    return second_largest

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(second_largest(arr))
