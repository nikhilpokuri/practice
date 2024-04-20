import re
t = int(input())
for _ in range(t):
    num = input()
    pattern = r"^[+-.]?\d*\.\d+$"
    if re.match(pattern, num):
        print(True)
    else:
        print(False)