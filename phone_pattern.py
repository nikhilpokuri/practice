import re
n = int(input())
for _ in range(n):
    num = input()
    if len(num) != 10:
        print("NO")
    else:
        pattern = r"^[789]\d{8}"
        chk = re.match(pattern, num)
        # print(chk)
        if chk:
            print("YES")
        else:
            print("NO")