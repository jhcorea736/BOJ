dict = { "a": "4", "e": "3", "i": "1", "o": "0", "s": "5" }

print("".join([dict[d] if d in dict else d for d in list(input())]))