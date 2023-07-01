from collections import Counter
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    data = []
    
    for __ in range(int(input())):
        wear_name, wear_type = input().split()
        data.append(wear_type)

    wear_dict = Counter(data)
    cnt = 1

    for wear in wear_dict:
        cnt *= wear_dict[wear] + 1
    
    print(cnt - 1)