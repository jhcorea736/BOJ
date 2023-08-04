a = int(input())
x = int(input())
b = int(input())
y = int(input())
t = int(input())

result_a = a + max(t - 30, 0) * x * 21
result_b = b + max(t - 45, 0) * y * 21

print(result_a, result_b)