import sys
input = sys.stdin.readline

def factorial(n):
    if n == 0:
        return 1
    
    result = 1

    for num in range(1, n + 1):
        result *= num

    return result
    
print(factorial(int(input())))