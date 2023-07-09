import sys
input = sys.stdin.readline

n = int(input())

memo = [float('INF')] * (n + 1)
memo[0] = 0
memo[1] = 1

for i in range(2, n + 1):
    j = 1
    
    while j * j <= i:
        memo[i] = min(memo[i], memo[i - j * j] + 1)
        j += 1

print(memo[n])
