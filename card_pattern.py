import re
card = "5133-2367-8912-3456"
chk = card[0]
cnt = 1
for i in card[1:]:
    if i == '-':
        continue
    if chk[-1] == i:
        cnt += 1
        if cnt == 4:
            print("Invalid")
            break
    else:
        chk = i
        cnt = 1
else:      
    pattern = r'^(?!.*(\d)\1{3})[456]\d{3}-?\d{4}-?\d{4}-?\d{4}'
    if re.match(pattern,card):
        print("VALID")
    else:
        print("INVALID")