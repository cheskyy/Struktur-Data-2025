from collections import deque

while True:
    try:
        s = input()
        if not s:
            break

        L = deque()
        p_front = True

        for char in s:
            if char == '[':
                p_front = True
            elif char == ']':
                p_front = False
            else:
                if p_front:
                    L.appendleft(char)
                else:
                    L.append(char)

        print(''.join(L))

    except EOFError:
        break
