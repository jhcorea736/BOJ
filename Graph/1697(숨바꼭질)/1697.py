from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
queue = deque()
queue.append(n)
visited = [0] * 100001

def bfs():
    while queue:
        position = queue.popleft()

        if position == k:
            return visited[position]

        for next_position in (position - 1, position + 1, position * 2):
            if 0 <= next_position <= 100000 and visited[next_position] == 0:
                visited[next_position] = visited[position] + 1
                queue.append(next_position)

print(bfs())