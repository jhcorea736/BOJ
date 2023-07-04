import sys
input = sys.stdin.readline

def dfs(start):
    global cnt
    visited[start] = True

    for i in graph[start]:
        if visited[i] == False:
            dfs(i)
            cnt += 1

node = int(input())
edge = int(input())
graph = [[] for _ in range(node + 1)]
visited = [False] * (node + 1)
cnt = 0

for _ in range(edge):
    src, dest = map(int, input().split())
    graph[src].append(dest)
    graph[dest].append(src)

dfs(1)
print(cnt)