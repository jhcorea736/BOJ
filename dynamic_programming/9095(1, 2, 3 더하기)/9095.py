import sys
input = sys.stdin.readline

memo = [0] * 100
memo[:3] = [1, 1, 1]

for i in range(3, 100):
    memo[i] = memo[i - 2] + memo[i - 3]

for _ in range(int(input())):
    print(memo[int(input()) - 1])