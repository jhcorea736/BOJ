import sys
input = sys.stdin.readline
n = int(input())

memo = [0] * (n + 1)
memo[0] = 1
memo[1] = 1

for i in range(2, n + 1):
    memo[i] = (memo[i - 1] + 2 * memo[i - 2]) % 10007

print(memo[n])