n = int(input())
result = 0

for i in range(1, n + 1):
    num = i
    digits = num

    while num > 0:
        digits += num % 10
        num //= 10
    
    if digits == n:
        result = i
        break

print(result)