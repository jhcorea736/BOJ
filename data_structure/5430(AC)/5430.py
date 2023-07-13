from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    p = input().rstrip()
    n = int(input())
    queue = deque(input().rstrip()[1:-1].split(','))
    is_reverse = False

    if n == 0:
        queue = deque()
    
    for op in p:
        if op == 'R':
            is_reverse = not is_reverse
        elif op == 'D':
            if not queue:
                print('error')
                break
            if is_reverse:
                queue.pop()
            else:
                queue.popleft()
    else:
        print("[" + ",".join(reversed(queue) if is_reverse else queue) + ']')