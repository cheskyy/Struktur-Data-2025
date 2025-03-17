a = int(input())
queue = []

for i in range(a):
    perintah = input() 
    if perintah[0]=="+":
        queue.append(perintah[1:])
    elif queue:
        queue.pop(0)
    else:
        print("kosong")
    print(queue)