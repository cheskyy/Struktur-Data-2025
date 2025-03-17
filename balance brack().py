kurung = input()

pasangan = {
    ')':'(',
    ']':'[',
    '}':'{'
}

stack = []

for i in kurung:
    if i in "([{":
        stack.append(i)
    else:
        if not stack or stack[-1] != pasangan[i]:
            print("no")
            exit()
        stack.pop()
if not stack:
    print('yes')
else:
    print('no')