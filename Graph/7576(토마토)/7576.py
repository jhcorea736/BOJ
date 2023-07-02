from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

queue = deque()
result = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(m):
        if data[i][j] == 1:
            queue.append((i, j))

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if 0 <= nx < n and 0 <= ny < m and data[nx][ny] == 0:
            data[nx][ny] = data[x][y] + 1
            queue.append((nx, ny))

if any(0 in datum for datum in data):
    result = -1
else:
    result = max(map(max, data)) - 1

print(result)