import sys
n = int(sys.stdin.readline())

cnt = 0
data = 666

while n > cnt:
    if '666' in str(data):
        cnt += 1
        
    data += 1

print(data - 1)
