import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0 

def dfs(x, y):
    if 0 <= x < n and 0 <= y < m and graph[x][y] != 'X' and visited[x][y] == False:
        visited[x][y] = True

        if graph[x][y] == 'P':
            global cnt
            cnt += 1

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            dfs(nx, ny)

for x in range(n):
    for y in range(m):
        if graph[x][y] == 'I':
            dfs(x, y)

if cnt <= 0:
    print('TT')
else:
    print(cnt)