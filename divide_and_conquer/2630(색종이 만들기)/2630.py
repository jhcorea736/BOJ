import sys
input = sys.stdin.readline

def cut(x, y, n):
    if n == 1:
        return (0, 1) if data[x][y] == 1 else (1, 0)
    
    mid = n // 2
    
    top_left = cut(x, y, mid)
    top_right = cut(x, y + mid, mid)
    bottom_left = cut(x + mid, y, mid)
    bottom_right = cut(x + mid, y + mid, mid)

    white_count = top_left[0] + top_right[0] + bottom_left[0] + bottom_right[0]
    blue_count = top_left[1] + top_right[1] + bottom_left[1] + bottom_right[1]

    if white_count == 0:
        blue_count = 1
    elif blue_count == 0:
        white_count = 1

    return white_count, blue_count

data = []
n = int(input())

for _ in range(n):
    temp = list(map(int, input().split()))
    data.append(temp)

white_count, blue_count = cut(0, 0, n)

print(white_count)
print(blue_count)