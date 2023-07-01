import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = {}

for _ in range(n):
    domain, password = input().split()
    data[domain] = password
    data[password] = domain

for _ in range(m):
    print(data[input().rstrip()])