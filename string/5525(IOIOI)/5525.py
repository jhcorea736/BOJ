import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().rstrip()

result = cnt = i = 0

while i < m - 1:
    if s[i:i + 3] == "IOI":
        cnt += 1
        i += 2

        if cnt == n:
            cnt -= 1
            result += 1
    else:
        cnt = 0
        i += 1

print(result)