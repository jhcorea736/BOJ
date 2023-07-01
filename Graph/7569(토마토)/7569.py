from collections import deque
import sys
input = sys.stdin.readline

m, n, h = map(int, input().split())

queue = deque()
data = []
visited = []
result = 0

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

for _ in range(h):
    for __ in range(n):
        data.append(list(map(int, input().split())))
        visited.append([False] * m)

def bfs():
    print()