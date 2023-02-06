n="{[()]}"
stack=[]
lib={'[':']','(':')','{':'}'}
for i in n:
    if i in ['{','[','(']:
        stack.append(i)
    else:
        if stack:
            top=stack.pop()
            if lib[top]!=i:
                print(False)
                break
        else:
            print(False)
            break

if stack:
    print(False)
else:
    print(True)
