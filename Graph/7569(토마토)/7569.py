from collections import deque
import sys
input = sys.stdin.readline

m, n, h = map(int, input().split())
data = [[list(map(int, input().split())) for _ in range(n)] for __ in range(h)]

queue = deque()
result = 0

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

for i in range(h):
    for j in range(n):
        for k in range(m):
            if data[i][j][k] == 1:
                queue.append((i, j, k))

while queue:
    x, y, z = queue.popleft()

    for i in range(6):
        nx = dx[i] + x
        ny = dy[i] + y
        nz = dz[i] + z

        if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and data[nx][ny][nz] == 0:
            data[nx][ny][nz] = data[x][y][z] + 1
            queue.append((nx, ny, nz))

flag = False

for i in range(h):
    for j in range(n):
        for k in range(m):
            if data[i][j][k] == 0:
                flag = True
            result = max(result, data[i][j][k])

print(-1 if flag else result - 1)