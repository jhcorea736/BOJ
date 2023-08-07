data = input()
result = len(data) + data.count(':') + data.count('_') * 5

print(result)