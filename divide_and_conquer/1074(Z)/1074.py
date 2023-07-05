import sys
input = sys.stdin.readline

def visit_count(n, r, c):
    if n == 0:
        return 0
    
    size = 2 ** (n - 1)
    quadrant_size = size ** 2

    if r < size and c < size:
        return visit_count(n - 1, r, c)
    elif r < size and c >= size:
        return quadrant_size + visit_count(n - 1, r, c - size)
    elif r >= size and c < size:
        return 2 * quadrant_size + visit_count(n - 1, r - size, c)
    else:
        return 3 * quadrant_size + visit_count(n - 1, r - size, c - size)
    
n, r, c = map(int, input().split())
print(visit_count(n, r, c))